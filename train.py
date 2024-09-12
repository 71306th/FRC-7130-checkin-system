from ultralytics import YOLO


model = YOLO('yolov8n.pt')


model.train(data=r'C:\Users\User\Desktop\FRC Note Detection.v8i.yolov8\data.yaml', epochs=200, imgsz=640, batch=32)