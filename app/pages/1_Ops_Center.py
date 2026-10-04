import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cv2, time, streamlit as st, pandas as pd, numpy as np
from detector import CottonWeedDetector, IntraRowEngine
from actuator import ActuationController
from pathlib import Path

st.set_page_config(page_title="CotWeed Gramin Sahayak", layout="wide", page_icon="🌱")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    background-color: #FAF9F6 !important;
}
.stApp { background-color: #FAF9F6; }

/* Hide default streamlit header */
header {visibility: hidden;}
.css-18ni7ap { display: none; }

/* Custom Top Bar */
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

/* Video Container */
.video-container {
    background: #FFFFFF;
    padding: 16px;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    border: 1px solid #E2E8F0;
    margin-bottom: 16px;
}

/* Action Buttons */
.stButton > button {
    border-radius: 8px !important;
    font-weight: 600 !important;
    padding: 10px 24px !important;
    border: none !important;
    transition: all 0.2s !important;
    width: 100% !important;
}
.btn-pause > button {
    background-color: #FFF7ED !important;
    color: #C2410C !important;
    border: 1px solid #FED7AA !important;
}
.btn-purge > button {
    background-color: #16A34A !important;
    color: #FFFFFF !important;
}

/* Summary Cards */
.summary-box {
    background: #FFFFFF;
    padding: 16px;
    border-radius: 12px;
    border: 1px solid #E2E8F0;
    text-align: center;
}
.sum-title { font-size: 11px; color: #64748B; font-weight: 600; margin-bottom: 4px; }
.sum-val { font-size: 24px; color: #0F172A; font-weight: 700; }

/* Nozzle Circles */
.nozzle-card {
    background: #F8FAFC;
    border-radius: 12px;
    padding: 16px;
    text-align: center;
    border: 1px solid #E2E8F0;
}
.nozzle-circle {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    margin: 0 auto 10px auto;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 12px;
}
.nz-active { background: #16A34A; color: white; box-shadow: 0 0 15px rgba(22, 163, 74, 0.4); }
.nz-idle { background: #FFFFFF; color: #64748B; border: 2px solid #CBD5E1; }

/* Helpline */
.helpline-box {
    background: #92400E;
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

# 1. TOP BAR
st.markdown("""
<div class="gs-top-bar">
    <div>
        <h1>CotWeed Gramin Sahayak</h1>
        <p>शेतात थेट फवारणी (Live Spray & Machine View)</p>
    </div>
    <div style="display:flex; gap: 10px; align-items:center;">
        <span style="background:#DCFCE7; color:#16A34A; padding:4px 10px; border-radius:20px; font-size:12px; font-weight:600;">🟢 LIVE</span>
        <span style="font-size:12px; color:#475569; font-weight:500;">EN | <b>मराठी</b></span>
    </div>
</div>
""", unsafe_allow_html=True)

if 'running' not in st.session_state: st.session_state.running = False
if 'savings_history' not in st.session_state: st.session_state.savings_history = []
if 'total_weeds' not in st.session_state: st.session_state.total_weeds = 0

with st.sidebar:
    st.markdown("### Settings")
    use_mock = st.checkbox("Demo Mode (MOCK)", value=True)
    corridor_pct = st.slider("Row Corridor Width (%)", 10, 60, 30, 5)
    trigger_pct = st.slider("Trigger Line (%)", 50, 90, 75, 5)
    num_nozzles = st.slider("Nozzle Array (valves)", 2, 8, 4, 1)

# 2. VIDEO FEED
st.markdown('<div class="video-container">', unsafe_allow_html=True)
video_placeholder = st.empty()
st.markdown('</div>', unsafe_allow_html=True)

# 3. ACTION BUTTONS
bc1, bc2 = st.columns(2)
with bc1:
    st.markdown('<div class="btn-pause">', unsafe_allow_html=True)
    if st.button("⏸ फवारणी तात्पुरती थांबवा (Pause Spray)"):
        st.session_state.running = not st.session_state.running
    st.markdown('</div>', unsafe_allow_html=True)
with bc2:
    st.markdown('<div class="btn-purge">', unsafe_allow_html=True)
    st.button("⏏️ नोजल साफ करा (Clear Nozzles / Purge)")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)

# 4. TODAY's SUMMARY (Metrics)
st.markdown("<h4 style='color:#0F172A; margin-bottom:12px;'>📊 आजचे काम व बचत (Today's Summary)</h4>", unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
metric_ph1 = m1.empty()
metric_ph2 = m2.empty()
metric_ph3 = m3.empty()
metric_ph4 = m4.empty()

def update_metrics(weeds, saved_pct, vol, fps):
    metric_ph1.markdown(f'<div class="summary-box"><div class="sum-title">तण मारले (Weeds Shot)</div><div class="sum-val">{weeds}</div></div>', unsafe_allow_html=True)
    metric_ph2.markdown(f'<div class="summary-box"><div class="sum-title">औषध बचत (Chem Saved)</div><div class="sum-val" style="color:#16A34A;">{saved_pct}%</div></div>', unsafe_allow_html=True)
    metric_ph3.markdown(f'<div class="summary-box"><div class="sum-title">वापरलेले औषध (Used)</div><div class="sum-val">{vol:.1f} ml</div></div>', unsafe_allow_html=True)
    metric_ph4.markdown(f'<div class="summary-box"><div class="sum-title">वेग (Speed)</div><div class="sum-val">{fps:.1f} fps</div></div>', unsafe_allow_html=True)

update_metrics(0, 0, 0, 0)

st.markdown("<br/>", unsafe_allow_html=True)

# 5. NOZZLE STATUS
st.markdown("<h4 style='color:#0F172A; margin-bottom:12px;'>🟢 नोजल स्थिती व सेन्सर रिपोर्ट (Nozzle Status)</h4>", unsafe_allow_html=True)
n_cols = st.columns(4)
nozzle_phs = [col.empty() for col in n_cols]

def render_nozzles(active_list, total):
    for i in range(1, total + 1):
        if i <= len(nozzle_phs):
            is_active = i in active_list
            cls = "nz-active" if is_active else "nz-idle"
            status = "Spraying" if is_active else "Ready"
            nozzle_phs[i-1].markdown(f"""
            <div class="nozzle-card">
                <div class="sum-title">Nozzle {i}</div>
                <div class="nozzle-circle {cls}">{'💧' if is_active else 'N'+str(i)}</div>
                <div style="font-size:11px; color:#64748B; font-weight:600;">{status}</div>
            </div>
            """, unsafe_allow_html=True)

render_nozzles([], num_nozzles)

# 6. HELPLINE
st.markdown("""
<div class="helpline-box">
    <div>
        <h4 style="margin:0; font-size:16px;">मशीनमध्ये काही अडचण आली का?</h4>
        <p style="margin:0; font-size:12px; opacity:0.9;">आमच्या कृषी तज्ज्ञांना कॉल करा (Helpline Toll Free)</p>
    </div>
    <div style="background:#FFFFFF; color:#92400E; padding:8px 16px; border-radius:20px; font-weight:bold; font-size:14px;">
        📞 1800-120-4050
    </div>
</div>
""", unsafe_allow_html=True)

if st.session_state.running:
    detector = CottonWeedDetector(use_mock=use_mock)
    intra_engine = IntraRowEngine(num_nozzles=num_nozzles, corridor_ratio=corridor_pct/100.0, trigger_ratio=trigger_pct/100.0)
    if 'controller' not in st.session_state: st.session_state.controller = ActuationController(num_nozzles=num_nozzles)
    controller = st.session_state.controller
    
    video_file = None
    for cand in ["data/sample.mp4", "sample.mp4", "field.mp4"]:
        if Path(cand).exists():
            video_file = cand
            break
            
    cap = cv2.VideoCapture(video_file) if video_file else None
    frame_idx, fps_t0 = 0, time.time()
    
    while st.session_state.running:
        if cap:
            ret, frame = cap.read()
            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
        else:
            frame = np.zeros((720, 1280, 3), dtype=np.uint8)
            frame[:] = (195, 215, 195)
            
        detections, latency = detector.detect(frame)
        roi = intra_engine.get_roi(frame.shape[1], frame.shape[0])
        
        triggered = []
        weed_c = sum(1 for d in detections if d.cls == 'weed')
        intra_c = sum(1 for d in detections if d.cls == 'weed' and intra_engine.is_intrarow(d, roi))
        
        for det in detections:
            if intra_engine.check_trigger(det, roi):
                ev = intra_engine.calculate_actuation(det, roi)
                controller.emit(ev)
                triggered.append(ev)
                
        controller.update_detection_stats(weed_c, intra_c)
        frame_idx += 1
        
        fps = 0
        if frame_idx % 10 == 0:
            fps = 10 / (time.time() - fps_t0 + 1e-6)
            fps_t0 = time.time()
            controller.update_perf(fps, latency)
        
        vis = intra_engine.draw_overlay(frame, detections, roi, triggered)
        vis_rgb = cv2.cvtColor(vis, cv2.COLOR_BGR2RGB)
        metrics = controller.get_metrics()
        
        video_placeholder.image(vis_rgb, channels="RGB", use_container_width=True)
        
        if frame_idx % 5 == 0:
            st.session_state.total_weeds = metrics["pulses_fired"]
            used_ml = metrics["pulses_fired"] * 0.08
            update_metrics(metrics["pulses_fired"], metrics["herbicide_saved_pct"], used_ml, fps)
            render_nozzles(metrics['recent_nozzles'], num_nozzles)
            
        time.sleep(0.02)
        
    if cap: cap.release()
