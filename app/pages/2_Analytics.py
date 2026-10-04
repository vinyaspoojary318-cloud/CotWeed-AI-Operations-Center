import streamlit as st
import time

st.set_page_config(page_title="Analytics - Gramin Sahayak", layout="wide", page_icon="💰")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    background-color: #FAF9F6 !important;
}
.stApp { background-color: #FAF9F6; }

header {visibility: hidden;}
.css-18ni7ap { display: none; }

.gs-top-bar {
    background: #FFFFFF;
    padding: 16px 24px;
    border-radius: 12px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    border-bottom: 2px solid #16A34A;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}
.gs-top-bar h1 { margin:0; font-size: 20px; color: #064E3B; font-weight: 700; }
.gs-top-bar p { margin:0; font-size: 12px; color: #64748B; }

.kpi-card {
    background: #FFFFFF;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #E2E8F0;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
}
.kpi-card.green { background: #16A34A; color: white; border: none; }
.kpi-card.green .kpi-title { color: #DCFCE7; }
.kpi-card.green .kpi-val { color: white; }

.kpi-title { font-size: 12px; color: #64748B; font-weight: 600; margin-bottom: 8px; }
.kpi-val { font-size: 28px; color: #0F172A; font-weight: 800; }

.tracker-box {
    background: #FFFFFF;
    padding: 24px;
    border-radius: 16px;
    border: 1px solid #E2E8F0;
    margin-top: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

.step-card {
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    padding: 16px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 12px;
}
.step-card.active {
    background: #DCFCE7;
    border: 1px solid #16A34A;
}
.step-icon {
    width: 40px; height: 40px; border-radius: 20px;
    background: #16A34A; color: white;
    display: flex; align-items: center; justify-content: center;
    font-weight: bold; font-size: 18px;
}
.step-icon.idle { background: #CBD5E1; color: #64748B; }

.helpline-box {
    background: #064E3B;
    color: white;
    padding: 16px 24px;
    border-radius: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 24px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="gs-top-bar">
    <div>
        <h1>CotWeed Gramin Sahayak</h1>
        <p>पैशांची बचत व हिशोब (Money Saved & Profits)</p>
    </div>
    <div style="display:flex; gap: 10px; align-items:center;">
        <span style="background:#DBEAFE; color:#1D4ED8; padding:4px 10px; border-radius:20px; font-size:12px; font-weight:600;">📊 ANALYTICS</span>
        <span style="font-size:12px; color:#475569; font-weight:500;">EN | <b>मराठी</b></span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<h4 style='color:#0F172A; margin-bottom:12px;'>💰 तुमची एकूण बचत (Your Savings)</h4>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
c1.markdown("""
<div class="kpi-card green">
    <div class="kpi-title">औषधाची बचत (Herbicide Saved)</div>
    <div class="kpi-val">₹ १,८४,५००</div>
</div>
""", unsafe_allow_html=True)

c2.markdown("""
<div class="kpi-card">
    <div class="kpi-title">वापरलेले औषध (Chemical Used)</div>
    <div class="kpi-val">४२ लिटर</div>
</div>
""", unsafe_allow_html=True)

c3.markdown("""
<div class="kpi-card">
    <div class="kpi-title">मशीनचा खर्च निघेल (ROI Payback)</div>
    <div class="kpi-val" style="color:#B45309;">३८ दिवसांत</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="tracker-box">
    <h4 style='color:#0F172A; margin-top:0;'>🏛 कृषी धोरणानुसार मिळणारी सूट (Maha-DBT Subsidy Tracker)</h4>
    <p style='color:#64748B; font-size:12px;'>तुम्ही ४०% अनुदानासाठी पात्र आहात. खालील प्रक्रिया पूर्ण करा.</p>
    
    <div class="step-card active">
        <div class="step-icon">✓</div>
        <div>
            <h5 style="margin:0; color:#16A34A;">१. शेतकरी नोंदणी (KYC Verified)</h5>
            <p style="margin:0; font-size:12px; color:#475569;">तुमचे आधार आणि 7/12 लिंक झाले आहे.</p>
        </div>
    </div>
    
    <div class="step-card">
        <div class="step-icon idle">२</div>
        <div>
            <h5 style="margin:0; color:#475569;">२. फवारणी रिपोर्ट अपलोड (Spray Log Sync)</h5>
            <p style="margin:0; font-size:12px; color:#64748B;">१५ दिवसांचा फवारणी रिपोर्ट सरकारला पाठवा.</p>
        </div>
    </div>
    
    <div class="step-card">
        <div class="step-icon idle">३</div>
        <div>
            <h5 style="margin:0; color:#475569;">३. बँक खात्यात जमा (Bank Deposit)</h5>
            <p style="margin:0; font-size:12px; color:#64748B;">४०% रक्कम (₹ १०,०००) खात्यात जमा होईल.</p>
        </div>
    </div>
    
    <button style="width:100%; background:#16A34A; color:white; border:none; padding:12px; border-radius:8px; font-weight:bold; margin-top:16px;">
        📥 फवारणी रिपोर्ट डाउनलोड करा (Download Report)
    </button>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="helpline-box">
    <div>
        <h4 style="margin:0; font-size:16px;">योजनेबद्दल शंका आहे का?</h4>
        <p style="margin:0; font-size:12px; opacity:0.9;">किसान हेल्पलाइन (Kisan Helpline)</p>
    </div>
    <div style="background:#FFFFFF; color:#064E3B; padding:8px 16px; border-radius:20px; font-weight:bold; font-size:14px;">
        📞 1800-120-4050
    </div>
</div>
""", unsafe_allow_html=True)
