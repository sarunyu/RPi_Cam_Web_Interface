#!/usr/bin/env python3

import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'subject'
    msg['From'] = 'e@mail.cc'
    msg['To'] = 'e@mail.cc'

    text = MIMEText("smartcam")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('iot.raspberry001@gmail.com','iot@1234')
    s.sendmail('iot.raspberry001@gmail.com','iot.raspberry001@gmail.com', msg.as_string())
    s.quit()

if __name__ == '__main__':
    SendMail(sys.argv[1])
