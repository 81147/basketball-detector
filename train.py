from ultralytics import YOLO
from pathlib import Path

ROOT = Path(__file__).parent
DATA_YAML=ROOT/"dataset"/"data.yaml"
if __name__ =="__main__":
    model = YOLO("yolov8n.pt")
    model.train(
        data=str(DATA_YAML),
        epochs=40,
        imgsz=640,
        batch=16,
        device=0,
        project=ROOT/"runs",
        name="basketball_yolov8n"
    )
