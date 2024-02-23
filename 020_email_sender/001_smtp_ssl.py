import smtplib, ssl

port = 465
password_input = input('Enter password: ')

# Create secure ssl context
context = ssl.create_default_context()

with smtplib.SMTP_SSL('EMAIL SERVER', port, context=context) as server:
    server.login('SENDERS EMAIL', password_input)
