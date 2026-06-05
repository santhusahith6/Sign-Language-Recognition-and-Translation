from ultralytics import YOLO
import streamlit as st
# Load the YOLO model
model = YOLO(r"C:\Users\DELL\Downloads\PT-1\PT-1\runs\detect\train8\weights\best.pt")

def run_detection_on_frame(frame):
    results = model.predict(source=frame, conf=0.25, verbose=False)
    boxes = results[0].boxes
    if boxes is not None and boxes.xyxy is not None and len(boxes) > 0:
        annotated_frame = results[0].plot()
    else:
        annotated_frame = frame
    return annotated_frame

