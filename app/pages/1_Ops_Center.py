import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import cv2, time, streamlit as st, pandas as pd, numpy as np
from detector import CottonWeedDetector, IntraRowEngine
from actuator import ActuationController
from pathlib import Path

st.set_page_config(page_title="Ops Center | RISE CotWeed", layout="wide", page_icon="🚜")

st.markdown("""
<style>
/* Hide Streamlit default header, footer, and menu */
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}

/* Modern Font */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background-color: #F3F4F6 !important;
}

/* Make main block fill screen and give it a premium background */
.stApp {
    background-color: #F3F4F6;
}

/* Premium Cards */
.metric-card {
    background-color: #FFFFFF;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    border: 1px solid #E5E7EB;
    border-left: 5px solid #16A34A; /* Modern Green */
    margin-bottom: 16px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -2px rgba(0, 0, 0, 0.04);
}
.metric-title { 
    font-size: 13px; 
    color: #6B7280; 
    font-weight: 600; 
    text-transform: uppercase; 
    letter-spacing: 0.05em; 
    margin-bottom: 8px;
}
.metric-value { 
    font-size: 28px; 
    color: #111827; 
    font-weight: 700; 
}

/* Buttons */
.stButton > button {
    border-radius: 8px !important;
    font-weight: 600 !important;
    padding: 0.5rem 1rem !important;
    border: none !important;
    transition: all 0.2s !important;
}
.stButton > button[kind="primary"] {
    background-color: #16A34A !important;
    color: white !important;
    box-shadow: 0 4px 6px -1px rgba(22, 163, 74, 0.2) !important;
}
.stButton > button[kind="primary"]:hover {
    background-color: #15803D !important;
    transform: translateY(-1px);
}

/* Console */
.console-box {
    background-color: #1F2937;
    border-radius: 12px;
    padding: 16px;
    font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace;
    font-size: 13px;
    color: #10B981;
    height: 200px;
    overflow-y: auto;
    box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.06);
    white-space: pre-wrap;
}

/* Custom Top Bar Replacement */
.css-18ni7ap {
    display: none;
}
</style>
""", unsafe_allow_html=True)

def render_nozzle_map(nozzles_active, total_nozzles):
    html = '<div style="display: flex; gap: 4px; padding: 10px; background: white; border-radius: 8px; border: 1px solid #E0E0E0; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin-bottom: 15px;">'
    for i in range(1, total_nozzles + 1):
        bg = "#FF5722" if i in nozzles_active else "#E0E5D5"
        color = "white" if i in nozzles_active else "#666"
        html += f'<div style="flex: 1; height: 24px; background: {bg}; color: {color}; text-align: center; border-radius: 4px; font-size: 12px; line-height: 24px; font-weight: bold;">N{i}</div>'
    html += '</div>'
    return html

with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Circle-icons-leaf.svg/200px-Circle-icons-leaf.svg.png", width=50)
    st.title("Ops Center")
    
    st.markdown("### Video Source")
    video_mode = st.radio("Select Source", ["Sample Field Video", "Upload MP4", "Webcam"], label_visibility="collapsed")
    uploaded_file = None
    if video_mode == "Upload MP4":
        uploaded_file = st.file_uploader("Upload a field video (.mp4)", type=["mp4", "avi", "mov"])
        if uploaded_file:
            temp_path = f"/tmp/{uploaded_file.name}"
            try:
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.read())
            except Exception:
                # Fallback for Windows if /tmp doesn't exist
                temp_path = f"data/{uploaded_file.name}"
                os.makedirs("data", exist_ok=True)
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.read())
            st.session_state.uploaded_video_path = temp_path

    st.markdown("---")
    st.markdown("### Equipment Settings")
    use_mock = st.checkbox("Demo Mode (MOCK)", value=True)
    multispectral = st.checkbox("🔮 Multispectral Vision (Night)", value=False)
    corridor_pct = st.slider("Row Corridor Width (%)", 10, 60, 30, 5)
    trigger_pct = st.slider("Trigger Line (%)", 50, 90, 75, 5)
    num_nozzles = st.slider("Nozzle Array (valves)", 2, 8, 4, 1)

    st.markdown("---")
    st.markdown("### 🌤️ Live Environment (Nagpur)")
    
    import requests
    @st.cache_data(ttl=600)
    def get_live_weather():
        try:
            # Open-Meteo API for Nagpur (no API key required)
            url = "https://api.open-meteo.com/v1/forecast?latitude=21.1458&longitude=79.0882&current=temperature_2m,relative_humidity_2m,wind_speed_10m&wind_speed_unit=kmh"
            res = requests.get(url, timeout=5).json()
            return {
                "temp": res["current"]["temperature_2m"],
                "humidity": res["current"]["relative_humidity_2m"],
                "wind": res["current"]["wind_speed_10m"]
            }
        except Exception:
            # Fallback if offline
            return {"temp": 32.5, "humidity": 45, "wind": 15.2}

    weather = get_live_weather()
    c_w1, c_w2 = st.columns(2)
    c_w1.metric("🌡️ Temp", f"{weather['temp']}°C")
    c_w2.metric("💨 Wind", f"{weather['wind']} km/h")
    
    wind_speed = weather['wind']
    
    if wind_speed > 20:
        st.error("⚠️ HIGH DRIFT RISK")
        drift_factor = 0.5
    elif wind_speed > 12:
        st.warning("Medium Drift Risk")
        drift_factor = 0.8
    else:
        st.success("Ideal Spray Conditions")
        drift_factor = 1.0

st.markdown("""
<div class="top-bar" style="background: #FFFFFF; padding: 16px 24px; border-radius: 16px; box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06); margin-bottom: 24px; display: flex; align-items: center; border: 1px solid #E5E7EB; justify-content: space-between;">
    <div style="display:flex; align-items:center;">
        <h1 style="margin: 0; padding: 0; font-size: 24px; color: #111827; font-weight: 700;">CotWeed AI Operations Center</h1>
        <span style="margin-left: 12px; padding: 4px 10px; background: #DCFCE7; color: #16A34A; border-radius: 9999px; font-size: 12px; font-weight: 600;">LIVE DEMO</span>
    </div>
    <div style="color: #6B7280; font-size: 14px; font-weight: 500;">Gramin Sahayak V2</div>
</div>
""", unsafe_allow_html=True)

if 'running' not in st.session_state: st.session_state.running = False
if 'savings_history' not in st.session_state: st.session_state.savings_history = []

c1, c2, c3 = st.columns([1, 1, 4])
with c1:
    if st.button("▶️ START OPERATION", use_container_width=True, type="primary"): st.session_state.running = True
with c2:
    if st.button("⏹ STOP", use_container_width=True): st.session_state.running = False

col_main, col_side = st.columns([2.5, 1])

with col_main:
    video_placeholder = st.empty()
    st.markdown("#### Herbicide Saved % (Last 60s)")
    chart_placeholder = st.empty()

with col_side:
    st.markdown("#### Implement Status")
    map_placeholder = st.empty()
    m1 = st.empty()
    m2 = st.empty()
    calc_placeholder = st.empty()
    st.markdown("#### Controller Log")
    console_placeholder = st.empty()

if st.session_state.running:
    detector = CottonWeedDetector(use_mock=use_mock)
    intra_engine = IntraRowEngine(num_nozzles=num_nozzles, corridor_ratio=corridor_pct/100.0, trigger_ratio=trigger_pct/100.0)
    if 'controller' not in st.session_state: st.session_state.controller = ActuationController(num_nozzles=num_nozzles)
    controller = st.session_state.controller
    
    video_file = None
    if video_mode == "Upload MP4":
        video_file = st.session_state.get('uploaded_video_path', None)
    elif video_mode == "Sample Field Video":
        for cand in ["data/sample.mp4", "sample.mp4", "field.mp4"]:
            if Path(cand).exists():
                video_file = cand
                break
                
    if video_mode == "Webcam":
        cap = cv2.VideoCapture(0)
    else:
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
        
        # --- Multispectral Feature ---
        if multispectral:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.applyColorMap(gray, cv2.COLORMAP_TURBO)
            
        triggered = []
        weed_c = sum(1 for d in detections if d.cls == 'weed')
        intra_c = sum(1 for d in detections if d.cls == 'weed' and intra_engine.is_intrarow(d, roi))
        
        for det in detections:
            if intra_engine.check_trigger(det, roi):
                ev = intra_engine.calculate_actuation(det, roi)
                # --- Wind Drift Mitigation Feature ---
                ev.pulse_ms = max(10, int(ev.pulse_ms * drift_factor))
                
                controller.emit(ev)
                triggered.append(ev)
                
        controller.update_detection_stats(weed_c, intra_c)
        frame_idx += 1
        
        if frame_idx % 10 == 0:
            fps = 10 / (time.time() - fps_t0 + 1e-6)
            fps_t0 = time.time()
            controller.update_perf(fps, latency)
        else:
            controller.update_perf(0, latency)
            
        vis = intra_engine.draw_overlay(frame, detections, roi, triggered)
        vis_rgb = cv2.cvtColor(vis, cv2.COLOR_BGR2RGB)
        metrics = controller.get_metrics()
        
        saved_pct = metrics['herbicide_saved_pct']
        if frame_idx % 10 == 0:
            st.session_state.savings_history.append(saved_pct)
            if len(st.session_state.savings_history) > 60:
                st.session_state.savings_history.pop(0)

        with col_main:
            video_placeholder.image(vis_rgb, channels="RGB", use_container_width=True)
            if len(st.session_state.savings_history) > 0:
                df = pd.DataFrame(st.session_state.savings_history, columns=['Saved %'])
                chart_placeholder.area_chart(df, height=120, use_container_width=True, color="#8BC34A")

        with col_side:
            map_placeholder.markdown(render_nozzle_map(metrics['recent_nozzles'], num_nozzles), unsafe_allow_html=True)
            m1.markdown(f'<div class="metric-card"><div class="metric-title">🌿 Weeds Treated</div><div class="metric-value">{metrics["pulses_fired"]}</div></div>', unsafe_allow_html=True)
            m2.markdown(f'<div class="metric-card"><div class="metric-title">💧 Chem Saved (%)</div><div class="metric-value">{saved_pct}%</div></div>', unsafe_allow_html=True)
            
            log_text = "\n".join([f"[{l['ts']}] {l['track_id']} N{l['nozzle_id']} {l['pulse_ms']}ms {l.get('occ_flag','')}" for l in list(controller.event_log)[:10]])
            console_placeholder.markdown(f'<div class="console-box">{log_text or "Awaiting weeds..."}</div>', unsafe_allow_html=True)
            
        time.sleep(0.03)
        
    if cap: cap.release()
else:
    with col_main:
        st.info("System Ready. Press Start Operation.")
