# AI-Powered Precision Intra-Row Weeder for Cotton Farming
### Nagpur RISE Hackathon - Vidarbha Agri Innovation Cohort

Production-ready software prototype for intelligent perception + actuation controller for autonomous rover / smart tractor implement.

## Architecture
```
Down-facing Camera (video/webcam)
        ↓
CottonWeedDetector (YOLOv8n/v11 or Mock)
        ↓
IntraRowEngine
 - Dynamic ROI: Intra-Row Corridor (center strip) vs Inter-Row Alley
 - Actuation Trigger Line (Y=75%)
 - Nozzle Mapping (N1..N4) + Pulse Duration from bbox area
        ↓
ActuationController
 - JSON payload -> ESP32 (Serial/MQTT)
 - Telemetry: weeds, pulses, herbicide saved 80%+, FPS/latency
        ↓
Streamlit Dashboard (EN/MR/HI)
```

## Quick Start (3-min demo)

### 1. Install
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run WITHOUT custom model (uses MOCK detector - jury ready)
```bash
streamlit run app/main.py
# Tick "Force MOCK Detector" in sidebar
# Select "Sample Field Video" or "Webcam"
# Press Start
```

### 3. Run WITH Roboflow pre-trained model

**Option A - Download from Roboflow Universe:**
1. Go to Roboflow Universe and search: `CottonWeedDet12` or `cotton-weed detection`
2. Download dataset model: Export as YOLOv8, download `best.pt`
3. Place it:
```bash
mkdir -p models
mv ~/Downloads/best.pt models/best.pt
```

**Option B - Train your own from Roboflow:**
```python
# roboflow_train.py
from roboflow import Roboflow
rf = Roboflow(api_key="YOUR_KEY")
project = rf.workspace("your-workspace").project("cotton-weed")
dataset = project.version(2).download("yolov8")
# Then train
from ultralytics import YOLO
model = YOLO('yolov8n.pt')
model.train(data=f"{dataset.location}/data.yaml", epochs=50, imgsz=640)
# best.pt will be in runs/detect/train/weights/best.pt
```

Then run:
```bash
streamlit run app/main.py
# Uncheck MOCK, model auto-loads from models/best.pt
```

### 4. Using any sample field video
- Record down-facing video walking along cotton rows (720p, 30fps ideal)
- Or use: `data/sample.mp4`
- Upload via sidebar "Upload MP4"

Supported: mp4, avi, mov. Traversing speed ~0.5 m/s simulation.

## Actuation JSON (ESP32 interface)

Payload emitted on trigger:
```json
{
  "timestamp": "2026-05-13T14:22:10.123Z",
  "nozzle_id": 2,
  "pulse_ms": 75,
  "x_offset_px": -120,
  "weed_area_px": 1420,
  "confidence": 0.89,
  "is_intrarow": true,
  "herbicide_ml": 6.0,
  "cmd": "SOLENOID:2:PULSE:75ms"
}
```

**ESP32 Arduino Snippet:**
```cpp
// Subscribe MQTT: weeder/nozzle/+
void callback(char* topic, byte* payload, unsigned int length) {
  DynamicJsonDocument doc(512);
  deserializeJson(doc, payload);
  int nozzle = doc["nozzle_id"];
  int pulse = doc["pulse_ms"];
  digitalWrite(nozzlePins[nozzle-1], HIGH);
  delay(pulse);
  digitalWrite(nozzlePins[nozzle-1], LOW);
}
```

Serial alternative: `Serial.println(jsonString)`

## Tuning for Vidarbha Cotton

- Row spacing: 90-120cm typical for Bt cotton
- Corridor width: 25-35% = intra-row strip where cotton stem grows
- Trigger line: 70-80% = gives 150ms time-to-spray for valve
- Pulse: 40-180ms (40=small weed, 180=large)
- Chemical saving calc: `saved% = 1 - (precision_used / broadcast_estimate)` -> target 80%

## Folder Structure
```
nagpur_rise_weeder/
├── app/
│   ├── detector.py  # Core vision & intra-row tracking
│   ├── actuator.py  # Telemetry & ESP32 payload
│   └── main.py      # Streamlit dashboard
├── models/          # Place best.pt here
├── data/            # sample field videos
├── requirements.txt
└── README.md
```

## Jury Pitch (3 min)
1. Problem: 30% yield loss due to intra-row weeds, labour shortage in Vidarbha
2. Demo: Live video -> red boxes on weeds, corridor overlay, trigger firing, console log
3. Impact: 80% herbicide reduction, precise actuation preserves cotton, Marathi/Hindi UI for farmers
4. Next: Integrate with Rover (Jetson Nano + ESP32 solenoid), add depth for laser weeding

Built for cotton value chain.
