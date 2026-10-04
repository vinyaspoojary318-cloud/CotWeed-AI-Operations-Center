"""
Roboflow Integration Helper
Run: python roboflow_helper.py
"""
# To use real model:
# pip install roboflow
# Then uncomment below

# from roboflow import Roboflow
# rf = Roboflow(api_key="YOUR_ROBOFLOW_API_KEY")
# project = rf.workspace().project("cotton-weed-detection")
# version = project.version(12) # CottonWeedDet12
# dataset = version.download("yolov8")
# print(dataset.location)
#
# from ultralytics import YOLO
# model = YOLO("yolov8n.pt")
# model.train(data=f"{dataset.location}/data.yaml", epochs=60, imgsz=640, batch=16)
# model.val()
# # Copy best.pt to models/

# For quick inference test with best.pt:
from ultralytics import YOLO
import cv2

model_path = "models/best.pt"
try:
    model = YOLO(model_path)
    print(f"Model classes: {model.names}")
    # Test
    # results = model.predict("data/sample.mp4", conf=0.45, show=True)
except Exception as e:
    print(f"Place best.pt in models/ to test. Error: {e}")
