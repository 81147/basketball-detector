from ultralytics import YOLO
from pathlib import Path
import cv2
ROOT = Path(__file__).parent
model=YOLO("yolov8n.pt")
train_images=ROOT/"dataset"/"train"/"images"
img_path=next(train_images.glob("*.jpg"))
print("用图：",img_path)

results=model(str(img_path))
r=results[0]

print("检测到框数：",len(r.boxes))
print("xyxy:",r.boxes.xyxy)
print("conf:",r.boxes.conf)
print("cls:",r.boxes.cls)
print("names:",r.names)

annotated = r.plot()
save_path=ROOT/"debug"/"infer_one.jpg"
cv2.imwrite(str(save_path),annotated)
print("已保存",save_path)
