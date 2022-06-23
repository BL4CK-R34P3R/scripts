#!/usr/bin/env python3
################## IMPORTING ##########################
import smtplib
import os
from email.message import EmailMessage
#######################################################
email = 'b19cs020@nitm.ac.in'
password = 'b19cs020'
print(email)
semail =  input("reciever email:")
sub = input("subject: ")
body = input("body: ")
#with smtplib.SMTP('smtp.gmail.com',) as smtp:
#   smtp.login(email,password)
msg = EmailMessage()
msg['Subject'] = sub
msg['From'] = email
msg['To'] = semail
try:
    msg.set_content(body)
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(email,password)

        smtp.send_message(msg)
        print ('Mail sent succesfully')
#    smtp.sendmail('b19cs020@nitm.ac.in',semail,msg)
except:
    print('Couldnt send the mail')
