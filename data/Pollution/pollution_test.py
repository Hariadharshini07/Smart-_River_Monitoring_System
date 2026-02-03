import random
import time
from pollution_detection import detect_pollution
from alerts.alert_manager import send_email_alert, send_sms_alert

while True:
    ph = round(random.uniform(6.0, 9.8), 2)
    turbidity = round(random.uniform(10, 45), 2)
    temperature = round(random.uniform(25, 45), 2)

    polluted, issues, severity = detect_pollution(ph, turbidity, temperature)

    print(f"pH: {ph}, Turbidity: {turbidity}, Temperature: {temperature}")

    if polluted:
        alert_msg = (
            f"🚨 POLLUTION ALERT\n"
            f"Severity: {severity}\n"
            f"Causes: {', '.join(issues)}"
        )
        print(alert_msg)

        if severity in ["MEDIUM", "HIGH"]:
            send_email_alert(alert_msg)
            send_sms_alert(alert_msg)
    else:
        print("✅ Water Quality Normal")

    print("-" * 60)
    time.sleep(3)
