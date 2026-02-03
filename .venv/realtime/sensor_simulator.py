import random
import time
import csv
from datetime import datetime

FILE = "data/sensor_log.csv"

# Create CSV header once
with open(FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "water_level", "turbidity", "plastic_density"])

while True:
    water_level = round(random.uniform(2.0, 8.0), 2)   # meters
    turbidity = round(random.uniform(10, 90), 2)       # NTU
    plastic = round(random.uniform(0, 1), 2)           # density %

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), water_level, turbidity, plastic])

    time.sleep(1)  # REAL TIME
