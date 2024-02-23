# python-learning@mrartful.com
# 8aS23!gh912

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465
context = ssl.create_default_context()
host = 'YOUR MAIL SERVER'
login = 'YOUR LOGIN'
password = 'YOUR PASSWORD'

message = MIMEMultipart()
message['Subject'] = 'Test email!'
message['From'] = login
message['To'] = 'RECIEVERS EMAIL'

text = '''Hi this message was sent by a script made with Python'''

html = '''<h1 style="color: red;">Hello world!</h1>'''

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

message.attach(part1)
message.attach(part2)

# message = 'Hello, I am a test message sent by Python.'

with smtplib.SMTP_SSL(host, port) as server:
    server.login(login, password)
    server.sendmail(login, 'RECIEVERS EMAIL', message.as_string())
