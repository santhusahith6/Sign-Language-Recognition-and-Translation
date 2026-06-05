# Sign Language Recognition using YOLOv8 and OpenCV

## Project Overview

This project is a real-time Sign Language Recognition System developed using YOLOv8 and OpenCV. The model is trained on sign language alphabet images and can detect and classify hand gestures from images, videos, or webcam input. The system aims to improve communication by recognizing sign language gestures accurately and efficiently.

## Features

- Real-time sign language detection using webcam
- YOLOv8-based object detection
- Image prediction support
- Custom dataset training
- Dataset preprocessing and splitting
- OpenCV integration for live video processing

## Project Structure

PT-1/
│
├── ownData/
│   ├── images/
│   │   ├── train/
│   │   └── val/
│   ├── labels/
│   │   ├── train/
│   │   └── val/
│
├── runs/
│
├── app.py
├── cv.py
├── sign.py
├── predict_image.py
├── preprocess.py
├── split_dataset.py
├── train_data.py
├── run_detection.py
├── test.py
│
├── dataset.yaml
├── ASL_Alphabet.jpg
├── images.jpg
│
├── yolov8n.pt
├── yolo11n.pt
│
└── README.md

## Technologies Used

- Python
- OpenCV
- YOLOv8 (Ultralytics)
- NumPy
- Pandas
- Matplotlib

## Installation

### Clone the Repository

git clone <repository-url>

cd PT-1

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

### Install Required Packages

pip install ultralytics opencv-python numpy pandas matplotlib

## Dataset Preparation

1. Place training and validation images inside:

ownData/images/

2. Place corresponding label files inside:

ownData/labels/

3. Configure dataset information and classes in:

dataset.yaml

## Training the Model

Run the following command:

python train_data.py

or

yolo task=detect mode=train data=dataset.yaml model=yolov8n.pt epochs=50

## Running Detection

### Webcam Detection

python run_detection.py

or

python cv.py

### Image Prediction

python predict_image.py

## Testing

python test.py

## Output

Training results and model weights are stored inside:

runs/detect/

The output includes:

- Trained model weights
- Performance metrics
- Confusion matrix
- Sample predictions

## Future Enhancements

- Sentence formation from detected signs
- Text-to-speech conversion
- Web application deployment
- Mobile application integration

## How to Execute in VS Code

1. Open VS Code.
2. Select File → Open Folder and open the PT-1 project folder.
3. Open Terminal by selecting Terminal → New Terminal.
4. Activate the virtual environment:

   venv\Scripts\activate

5. Install dependencies:

   pip install ultralytics opencv-python numpy pandas matplotlib

6. Train the model:

   python train_data.py

7. Run real-time sign language detection:

   python run_detection.py

   or

   python cv.py

8. Run image prediction:

   python predict_image.py

9. Run testing:

   python test.py

## Author

Kolluri Sahith

B.E. Computer Science and Engineering (AI & ML)

Sathyabama Institute of Science and Technology
