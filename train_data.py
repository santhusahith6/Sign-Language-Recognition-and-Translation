from ultralytics import YOLO

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()

    model = YOLO('yolov8n.yaml')  # You can change to yolov8s.yaml, yolov8m.yaml etc. for stronger models

    model.train(
        data="dataset.yaml",
        epochs=300,
        imgsz=640,
        batch=8,
        resume=True,
        device="0"  # <-- Use GPU device 0
    )

