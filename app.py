import streamlit as st
import cv2
import time
from run_detection import run_detection_on_frame  # Import the function from run_detection.py

# Streamlit UI setup
st.title("Real-Time ASL Hand Sign Detection")

st.write("This app runs a trained YOLOv8 model to detect ASL hand signs in real-time.")

# Create two columns for layout
left_column, right_column = st.columns([1, 3])

# Left column: Single image displaying ASL gestures
with left_column:
    st.header("ASL Hand Signs")

    # Display a single image with all ASL hand signs
    st.image(r"C:\Users\DELL\Downloads\PT-1\PT-1\ASL_Alphabet.jpg", caption="ASL Hand Signs", use_column_width=True)

# Right column: Detection and video feed
with right_column:
    st.header("Webcam Feed and Detection")

    # Variable to control the loop for detection
    is_detection_running = False

    # Placeholder to display the video feed
    frame_placeholder = st.empty()

    # Function to start the detection
    def start_detection():
        global is_detection_running
        is_detection_running = True

        # Capture webcam feed
        cap = cv2.VideoCapture(0)  # '0' is the default webcam

        if not cap.isOpened():
            st.error("Unable to access the webcam. Please check if it's connected properly.")
        else:
            # Loop to continuously grab frames from the webcam
            while is_detection_running and cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    st.error("Failed to read from webcam. Exiting...")
                    break

                # Process the frame through the YOLO model
                annotated_frame = run_detection_on_frame(frame)

                # Convert BGR (OpenCV format) to RGB for Streamlit display
                frame_placeholder.image(cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB), channels="RGB")

                # Add a small delay to control the frame rate
                time.sleep(0.03)  # Adjust for desired frame rate

            cap.release()  # Release the webcam when the loop ends

    # Function to stop the detection
    def stop_detection():
        global is_detection_running
        is_detection_running = False
        st.write("Detection stopped and webcam closed.")

    # Start detection button
    if st.button("Start Detection"):
        start_detection()

    # Stop detection button
    if st.button("Stop Detection"):
        stop_detection()
