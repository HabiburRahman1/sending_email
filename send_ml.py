import smtplib
import ssl
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import os
# Please 
email_sender = 'habib.usa2014@gmail.com'
email_password = 'zctosnbdyoaxwruj'
# Read CSV file and convert it to a dataframe
def read_csv(filename):
    """
    Read CSV file and convert it to a dataframe
    :param filename:
    :return:
    """
    df = pd.read_csv(filename)
    return df
def read_text_file(filename):
    """
    Read text file
    :param filename:
    :return:
    """
    with open(filename, 'r') as f:
        text = f.read()
    return text

def add_attachments(attachment_path, message):
    part = MIMEBase('application', "octet-stream")
    with open(attachment_path, 'rb') as ap:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(ap.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename={}'.format(Path(attachment_path).name))
    message.attach(part)
    return message

data_frame = read_csv('datos.csv')
csv_data_list = data_frame.values.tolist()
for csv_data in csv_data_list:
    name_email_data = csv_data[0].split(';')
    NOMBRE = name_email_data[0]
    DATO1 = name_email_data[2]
    email_receiver = name_email_data[1]
    email_body = read_text_file('plantilla.txt')
    body = email_body.format(NOMBRE=NOMBRE, DATO1=DATO1)
    subject = 'Please add your email subject here'
    # em = EmailMessage()
    em = MIMEMultipart()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em = add_attachments('pool.jpg', em)
    # em.set_content(body)
    em.attach(MIMEText(body))
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        # smtp.sendmail(email_sender, email_receiver, em.as_string())
        smtp.send_message(em)