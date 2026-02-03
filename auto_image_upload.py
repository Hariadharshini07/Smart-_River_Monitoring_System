import cv2
import time
import os

# Folder where images will be "uploaded"
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

cap = cv2.VideoCapture(0)

capture_interval = 5   # seconds
last_capture = 0

print("📸 Automatic image upload started... Press ESC to stop")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    current_time = time.time()

    # Auto capture every N seconds
    if current_time - last_capture >= capture_interval:
        filename = f"{UPLOAD_FOLDER}/image_{int(current_time)}.jpg"
        cv2.imwrite(filename, frame)
        print("📤 Image uploaded:", filename)
        last_capture = current_time

    cv2.imshow("Live Camera - Auto Upload", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
