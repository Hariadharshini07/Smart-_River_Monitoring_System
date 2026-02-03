import time
from datetime import datetime
from alert_email import send_email
from alert_sms import send_sms
import random  # Simulating sensor

FLOOD_LEVEL = 6.0  # meters

while True:
    # Simulate water level
    water_level = round(random.uniform(4.0, 8.0), 2)
    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    if water_level > FLOOD_LEVEL:
        message = f"""
🚨 FLOOD ALERT
Water Level: {water_level} m
Time      : {current_time}
"""
        send_sms(message)
        send_email(message)

    else:
        print(f"✅ Water Level Normal: {water_level} m at {current_time}")

    time.sleep(5)  # Check every 5 sec
