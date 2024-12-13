import smtplib
from email.mime.text import MIMEText

def send_email(sender_email, password, recipient_email, subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

send_email("your_email@gmail.com", "password", "recipient@example.com", "Subject", "Hello from Python!")
