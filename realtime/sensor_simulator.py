import random
import time
import csv
from datetime import datetime

FILE = "data/sensor_log.csv"

# Create CSV header
with open(FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "water_level", "turbidity", "plastic_density"])

print("🔴 Real-time sensor started...")

while True:
    water_level = round(random.uniform(2.0, 8.0), 2)
    turbidity = round(random.uniform(10, 90), 2)
    plastic = round(random.uniform(0, 1), 2)

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), water_level, turbidity, plastic])

    print("Live data →", water_level, turbidity, plastic)
    time.sleep(1)
