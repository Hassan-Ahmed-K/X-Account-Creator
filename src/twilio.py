from twilio.rest import Client

def twilio_recive_recent_msg():
    account_sid = 'AC8c19804bcf6c8642fc6c5fbff80e3f24'
    auth_token = '37e6701228327031d89c071ea5111ef6'
    client = Client(account_sid, auth_token)

    msg = client.messages.list(to="+19124726140")[0]

    return msg.body

# for msg in messages:
    # print(f"SID: {msg.sid}")
    # print(f"Date Sent: {msg.date_sent}")
    # print(f"From: {msg.from_}")
    # print(f"To: {msg.to}")
    # print(f"Status: {msg.status}")
    # print(f"Body: {msg.body}")
    # print(f"Price: {msg.price}")
    # print(f"Error Code: {msg.error_code}")
    # print(f"Error Message: {msg.error_message}")
    # print("-" * 40)
