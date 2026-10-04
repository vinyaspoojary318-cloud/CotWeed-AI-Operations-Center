import streamlit as st

st.set_page_config(page_title="Analytics | RISE CotWeed", layout="wide", page_icon="📊")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; background-color: #F3F4F6 !important; }
.stApp { background-color: #F3F4F6; }
.top-bar {
    background: #FFFFFF; padding: 16px 24px; border-radius: 16px;
    box-shadow: 0 1px 3px 0 rgba(0,0,0,0.1), 0 1px 2px 0 rgba(0,0,0,0.06);
    margin-bottom: 24px; border: 1px solid #E5E7EB;
}
.report-card {
    background: #FFFFFF; padding: 24px; border-radius: 16px;
    border: 1px solid #E5E7EB; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}
.stat-large { font-size: 36px; font-weight: 700; color: #16A34A; }
.stat-label { font-size: 14px; color: #6B7280; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }
.css-18ni7ap { display: none; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="top-bar">
    <h1 style="margin: 0; padding: 0; font-size: 24px; color: #111827; font-weight: 700;">Business & Impact Analytics</h1>
    <p style="margin: 5px 0 0 0; color: #6B7280; font-size: 14px;">Season projections based on live hardware telemetry.</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Circle-icons-leaf.svg/200px-Circle-icons-leaf.svg.png", width=50)
    st.markdown("### 💼 Cost Calculator")
    farm_size = st.number_input("Farm Size (Acres)", min_value=1, value=5)
    herb_cost = st.number_input("Herbicide (Rs/Litre)", min_value=100, value=1200)
    spray_rounds = st.number_input("Spray Rounds / Season", min_value=1, value=3)
    device_cost = st.number_input("Device Capex (Rs)", min_value=0, value=25000)
    
# Retrieve state if running
if 'controller' in st.session_state:
    metrics = st.session_state.controller.get_metrics()
    saved_pct = metrics['herbicide_saved_pct']
else:
    st.info("System is offline. Displaying projected baseline of 80% savings.")
    saved_pct = 80.0

broadcast_vol_per_acre = 2.0 
total_broadcast_vol = farm_size * broadcast_vol_per_acre * spray_rounds
total_broadcast_cost = total_broadcast_vol * herb_cost

est_saved_vol = total_broadcast_vol * (saved_pct / 100.0)
est_saved_rs = total_broadcast_cost * (saved_pct / 100.0)
roi_rs = est_saved_rs - device_cost
co2_saved = est_saved_vol * 2.3 # approx 2.3kg CO2 per litre of agrochemical

col1, col2 = st.columns([2, 1])

payback_days = int((device_cost / max(1, est_saved_rs)) * 120) if est_saved_rs > 0 else 0
payback_text = f"फक्त {payback_days} दिवसांत मशीन खर्च निघेल!" if payback_days > 0 else "मशीन खर्च एका हंगामात निघेल!"

with col1:
    st.markdown(f"""
    <div class="report-card">
        <h3 style="margin-top:0; color:#111827;">Season Financial Projection</h3>
        <p style="color:#D97706; font-weight:700; font-size:16px;">⏱️ Payback Estimate: {payback_text}</p>
        <div style="display:flex; justify-content:space-between; margin-top: 15px;">
            <div>
                <div class="stat-label">Total Chemical Saved</div>
                <div class="stat-large">{est_saved_vol:.1f} Litres</div>
            </div>
            <div>
                <div class="stat-label">Direct Money Saved</div>
                <div class="stat-large">₹{est_saved_rs:,.0f}</div>
            </div>
            <div>
                <div class="stat-label">Net ROI (1st Season)</div>
                <div class="stat-large" style="color:{'#16A34A' if roi_rs>0 else '#EF4444'};">₹{roi_rs:,.0f}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="report-card" style="border-left: 5px solid #059669;">
        <h3 style="margin-top:0; color:#111827;">🏛️ Maha-DBT / NABARD 40% Subsidy Tracker</h3>
        <p style="color: #6B7280; font-size:14px;">Track your ₹75,000 government hardware subsidy application.</p>
        
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top: 20px; padding: 15px; background: #F3F4F6; border-radius: 8px;">
            <div style="text-align:center; flex:1;">
                <div style="width:30px; height:30px; background:#16A34A; color:white; border-radius:50%; line-height:30px; margin:0 auto; font-weight:bold;">1</div>
                <div style="font-size:12px; font-weight:600; margin-top:5px; color:#111827;">KYC Verified</div>
            </div>
            <div style="flex:1; height:4px; background:#16A34A; margin: 0 10px;"></div>
            <div style="text-align:center; flex:1;">
                <div style="width:30px; height:30px; background:#16A34A; color:white; border-radius:50%; line-height:30px; margin:0 auto; font-weight:bold;">2</div>
                <div style="font-size:12px; font-weight:600; margin-top:5px; color:#111827;">Spray Log Sent</div>
            </div>
            <div style="flex:1; height:4px; background:#D1D5DB; margin: 0 10px;"></div>
            <div style="text-align:center; flex:1;">
                <div style="width:30px; height:30px; background:#D1D5DB; color:white; border-radius:50%; line-height:30px; margin:0 auto; font-weight:bold;">3</div>
                <div style="font-size:12px; font-weight:600; margin-top:5px; color:#6B7280;">Bank Deposit</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="report-card" style="background:#FFF7ED; border: 1px solid #FED7AA; border-left: 5px solid #F97316;">
        <h4 style="margin-top:0; color:#9A3412;">📞 24x7 Direct Kisan Helpline</h4>
        <p style="color: #C2410C; font-size:14px; margin-bottom: 5px;">Toll-Free Support for Farmers:</p>
        <h2 style="color:#C2410C; margin:0;">1800-120-4050</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="report-card">
        <h4 style="margin-top:0; color:#111827;">Export Report</h4>
        <p style="color: #6B7280; font-size:14px;">Generate an end-of-season PDF compliance report to claim your subsidy.</p>
    </div>
    """, unsafe_allow_html=True)
    st.download_button(
        label="📄 1-Click Apply & Print Receipt",
        data=f"Farm Size, {farm_size}\nSaved Litres, {est_saved_vol}\nSaved Rs, {est_saved_rs}\nCO2 Reduced, {co2_saved}",
        file_name="Subsidy_Receipt.csv",
        mime="text/csv",
        use_container_width=True
    )
