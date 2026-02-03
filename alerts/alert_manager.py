
from alerts.alert_manager import send_email_alert, send_sms_alert

def send_email_alert(message):
    print("📧 EMAIL ALERT SENT")
    print(message)

def send_sms_alert(message):
    print("📱 SMS ALERT SENT")
    print(message)

