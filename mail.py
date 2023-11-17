import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_address, subject, body, sender_address, sender_password):
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = to_address
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    session = smtplib.SMTP('smtp.gmail.com', 587)  
    session.starttls()  
    session.login(sender_address, sender_password)  
    text = message.as_string()
    session.sendmail(sender_address, to_address, text)
    session.quit()
