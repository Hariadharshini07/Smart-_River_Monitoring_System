import cv2

# IMAGE PATH
IMAGE_PATH = "images/test.jpg"
OUTPUT_PATH = "output/result.jpg"

# Read image
img = cv2.imread(IMAGE_PATH)

if img is None:
    print("❌ Image not found")
    exit()

# Dummy waste detection (rectangle)
h, w, _ = img.shape

# Draw bounding box (demo)
start_point = (int(w*0.1), int(h*0.4))
end_point = (int(w*0.9), int(h*0.9))
color = (0, 0, 255)  # Red
thickness = 3

cv2.rectangle(img, start_point, end_point, color, thickness)

# Label
cv2.putText(
    img,
    "WASTE DETECTED",
    (start_point[0], start_point[1] - 10),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.9,
    (0, 0, 255),
    2
)

# Save output
cv2.imwrite(OUTPUT_PATH, img)

print("✅ Waste detected and output saved")
print(f"📸 Output image: {OUTPUT_PATH}")
