import smtplib
import ssl

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define the transport variables
ctx = ssl.create_default_context()
password = "YOUR PASWORD"    # Your app password goes here
sender = "SENDER EMAIL"    # Your e-mail address
receiver = "RECIVER EMAIL" # Recipient's address

# Create the message
message = MIMEMultipart("mixed")
message["Subject"] = "Hello"
message["From"] = sender
message["To"] = receiver

# Attach message body content
message.attach(MIMEText("Hello from Python", "plain"))

# Attach image
filename = './images/mail.jpg'
with open(filename, "rb") as f:
    file = MIMEApplication(f.read())
disposition = f"attachment; filename={filename}"
file.add_header("Content-Disposition", disposition)
message.attach(file)

# Connect with server and send the message
with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())