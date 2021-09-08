import smtplib
import email.message

import smtplib
import email.message
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




def send_mail(to_address, subject, body):
    smtp_user = "raspsurvcam.com"
    smtp_password = "RaspSurvCam!"
    server = "smtp.gmail.com"
    port = 587

    #msg = MIMEMultipart("alternative")
    msg = email.message.Message()
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = to_address
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)
    s = smtplib.SMTP(server, port)
    s.starttls()
    s.login(smtp_user, smtp_password)
    s.sendmail(smtp_user, to_address, msg.as_string().encode('utf-8'))
    print("Sended")
    s.quit()
    
to_address = 'anaclara.aravecchia@gmail.com'
subject    = 'teste'
body       = '<p>Alo mundo</p>'
send_mail(to_address, subject, body)

