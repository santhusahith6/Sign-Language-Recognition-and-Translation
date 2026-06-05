import cv2
import numpy as np

def preprocess_frame(frame):
    frame = cv2.resize(frame, (28, 28))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = gray.reshape(1, 1, 28, 28).astype('float32') / 255.0
    return gray
