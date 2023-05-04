from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import smtplib
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('email.html')

# Set up the SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('ismaelrk41@gmail.com', 'situpugbjzoglaht')

# Compose the email message
sender_email = 'isamel41@gmail.com'
receiver_email = 'ismaelrakei41@gmail.com'
subject = 'Test Email'
body = 'This is a test email sent from Python.'
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Add attachments, if any
filename = 'example.txt'
if os.path.isfile(filename):
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")
    message.attach(part)

# Send the email
server.sendmail(sender_email, receiver_email, message.as_string())

# Close the SMTP connection
server.quit()
