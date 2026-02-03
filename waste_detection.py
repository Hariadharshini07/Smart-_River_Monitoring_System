import cv2
import time
from ultralytics import YOLO

# Load pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")   # light & fast

cap = cv2.VideoCapture(0)

last_capture = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    waste_detected = False
    detected_items = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            # Waste-related classes
            if label in ["plastic", "bottle", "cup", "trash", "garbage"]:
                waste_detected = True
                detected_items.append(label)

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,0,255), 2)
                cv2.putText(frame, label, (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

    # Auto image capture
    if waste_detected and time.time() - last_capture > 10:
        filename = f"waste_{int(time.time())}.jpg"
        cv2.imwrite(filename, frame)
        print("📸 Waste detected & image saved:", filename)
        print("Detected:", set(detected_items))
        last_capture = time.time()

    cv2.imshow("Waste Detection - Live", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
