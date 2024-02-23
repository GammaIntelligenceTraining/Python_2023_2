import smtplib, ssl
# NOTE that this message will not be delivered to GMAIL accounts
# ! message is not RFC 5322 compliant: 'From' header is missing.
# ! To reduce the amount of spam sent to Gmail, this message has been blocked

smtp_server = 'EMAIL SERVER'
port = 465
sender_email = 'SENDERS EMAIL'
password_input = input('Enter password: ')

reciever_email = 'RECIEVERS EMAIL'
message = 'Hello, this is a test message sent by python script.'

# Create secure ssl context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password_input)
    server.sendmail(sender_email, reciever_email, message)