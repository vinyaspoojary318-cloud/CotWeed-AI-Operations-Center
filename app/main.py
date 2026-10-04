import streamlit as st

st.set_page_config(page_title="RISE CotWeed", layout="wide", page_icon="🌱")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; background-color: #F3F4F6 !important; }
.stApp { background-color: #F3F4F6; }
.hero-box {
    background: #FFFFFF; padding: 40px; border-radius: 20px;
    box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); border: 1px solid #E5E7EB;
    text-align: center; margin-bottom: 30px;
}
.hero-title { font-size: 48px; font-weight: 800; color: #111827; letter-spacing: -0.02em; margin-bottom: 10px; }
.hero-subtitle { font-size: 20px; color: #16A34A; font-weight: 600; margin-bottom: 20px; }
.hero-desc { font-size: 16px; color: #6B7280; max-width: 600px; margin: 0 auto 30px auto; line-height: 1.6; }
.css-18ni7ap { display: none; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-box">
    <div class="hero-title">RISE CotWeed</div>
    <div class="hero-subtitle">Autonomous Precision Weeding for the Vidarbha Cotton Belt</div>
    <div class="hero-desc">
        Stop wasting money and poisoning soil with blanket herbicides. Our edge-AI system integrates with existing rovers to detect and target weeds with millimeter precision, achieving up to 80% chemical savings while protecting your crop.
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div style="background:#FFF; padding:24px; border-radius:16px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); border:1px solid #E5E7EB; text-align:center; height:200px;">
        <h2 style="font-size:36px; margin:0;">🎯</h2>
        <h3 style="color:#111827; font-size:18px;">Edge AI Vision</h3>
        <p style="color:#6B7280; font-size:14px;">Real-time centroid tracking and smart crop-occlusion algorithms ensure we never double-spray or damage the cotton.</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div style="background:#FFF; padding:24px; border-radius:16px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); border:1px solid #E5E7EB; text-align:center; height:200px;">
        <h2 style="font-size:36px; margin:0;">🌤️</h2>
        <h3 style="color:#111827; font-size:18px;">Smart Weather IoT</h3>
        <p style="color:#6B7280; font-size:14px;">Live integration with Open-Meteo dynamically adjusts nozzle pressure based on real-time wind speed to eliminate spray drift.</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div style="background:#FFF; padding:24px; border-radius:16px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); border:1px solid #E5E7EB; text-align:center; height:200px;">
        <h2 style="font-size:36px; margin:0;">💰</h2>
        <h3 style="color:#111827; font-size:18px;">Massive ROI</h3>
        <p style="color:#6B7280; font-size:14px;">Achieve an 80% reduction in chemical costs. The hardware pays for itself in a single 5-acre season.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)
st.info("👈 **Use the sidebar on the left** to navigate to the **Ops Center** (Live AI Demo) or **Analytics**.")
