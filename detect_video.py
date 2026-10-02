from pathlib import Path
import cv2
from ultralytics import YOLO

ROOT = Path(__file__).parent
VIDEO_IN = ROOT / "evaluation" / "basketball_dribble_evaluation.mp4"
VIDEO_OUT = ROOT / "result.mp4"
BEST_PT = ROOT / "model" / "best.pt"

model = YOLO(str(BEST_PT))

cap = cv2.VideoCapture(str(VIDEO_IN))
fps = cap.get(cv2.CAP_PROP_FPS)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter(str(VIDEO_OUT), fourcc, fps, (w, h))

trail = []
frame_idx = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.6)
    r = results[0]
    annotated = r.plot()

    boxes = r.boxes
    if len(boxes) > 0:
        idx = int(boxes.conf.argmax())
        x1, y1, x2, y2 = boxes.xyxy[idx].tolist()
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)
        trail.append((cx, cy))

    for i in range(1, len(trail)):
        cv2.line(annotated, trail[i-1], trail[i], (0, 255, 255), 4)

    if len(trail) > 0:
        text = f"center: ({trail[-1][0]}, {trail[-1][1]})"
        cv2.putText(annotated, text, (30, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 255), 4)

    writer.write(annotated)
    frame_idx += 1
    if frame_idx % 20 == 0:
        print("已处理", frame_idx, "帧")

cap.release()
writer.release()
print("完成，共", frame_idx, "帧，输出:", VIDEO_OUT)
