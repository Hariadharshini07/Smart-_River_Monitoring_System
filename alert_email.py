import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_SENDER = "hariadharshini.selvakumar.ct@gmail.com"
EMAIL_PASSWORD = "yeto thxw xiqq fzmx"
EMAIL_RECEIVER = "hariadharshini@gmail.com"
EMAIL_RECEIVER = "hariniharinisubramani2005@gmail.com"
def send_email_alert(subject, message):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

    print("EMAIL SENT SUCCESSFULLY")

# TEST
send_email_alert(
    "🚨 River Alert",
    "Sand theft detected near River Zone 2"
)
