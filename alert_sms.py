from twilio.rest import Client

# ====== TWILIO CONFIG ======
ACCOUNT_SID = "AC111f53a1d847a51bf425b28531afdcee"
AUTH_TOKEN = "acb247d67afe3a8566da376e2cf61670"

TWILIO_NUMBER = "+15202140980"
RECEIVER_NUMBER = "+919025586339"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_sms(message):
    msg = client.messages.create(
        body=message,
        from_=TWILIO_NUMBER,
        to=RECEIVER_NUMBER
    )
    print("SMS SENT ✔", msg.sid)


# TEST
if __name__ == "__main__":
    send_sms("🚨 Smart River Alert: SMS system working successfully!")
