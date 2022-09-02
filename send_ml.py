from io import BytesIO     # for handling byte strings
from io import StringIO    # for handling unicode strings
import smtplib
import ssl
from email.message import EmailMessage
import pandas as pd

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
data_frame = read_csv('datos.csv')
csv_data_list = data_frame.values.tolist()
for csv_data in csv_data_list:
    name_email_data = csv_data[0].split(';')
    print(name_email_data)
    NOMBRE = name_email_data[0]
    DATO1 = name_email_data[2]
    email_receiver = name_email_data[1]
    email_body = read_text_file('plantilla.txt')
    body = email_body.format(NOMBRE=NOMBRE, DATO1=DATO1)
    subject = 'Please add your email subject here'
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())