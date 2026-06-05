# from ultralytics import YOLO
# import cv2

# # Load your trained YOLOv8 model
# model = YOLO('D:/Ai-Projects/handSign1/last.pt')  # Make sure the path is correct

# # Load the image you want to detect objects in
# image_path = 'D:/Ai-Projects/handSign1/images.jpg'  # Ensure the image exists at this path
# image = cv2.imread(image_path)

# if image is None:
#     print(f"Error: Unable to load image from {image_path}")
#     exit()

# # Perform object detection on the image
# results = model.predict(source=image, conf=0.75, show=True)  # Lower confidence threshold to 0.25

# # Print detection results for debugging
# for result in results:
#     boxes = result.boxes.xyxy.cpu().numpy()  # Bounding boxes
#     confs = result.boxes.conf.cpu().numpy()  # Confidence scores
#     class_ids = result.boxes.cls.cpu().numpy()  # Class IDs
    
#     for box, conf, class_id in zip(boxes, confs, class_ids):
#         print(f"Detected {model.names[int(class_id)]} with confidence {conf:.2f} at {box}")

from ultralytics import YOLO

model = YOLO('D:/Ai-Projects/handSign1/last.pt')
results = model('D:/Ai-Projects/handSign1/images.jpg')
results.show()  # Visualize the results
