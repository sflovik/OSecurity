import smtplib
import os
import RPi.GPIO as GPIO
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import time
from time import sleep
import subprocess as sp


#Define variables for sender and reciever
fromaddr = "terminalnotificationstation@gmail.com"
toaddr = "cfthorne@hotmail.com"
ImgFileName = ('/home/pi/OSecuritySnapshots/faceFound.png')
msg = MIMEMultipart()
#Set sender
msg['From'] = fromaddr
#Set reciever
msg['To'] = toaddr
#Set subject line
msg ['Subject'] = "Bevegelse oppdaget - alarm"
#Define variable for email text
body = "Bevegelsessensoren har oppdaget anomaliteter."
msg.attach(MIMEText(body, 'plain'))
img_data = open(ImgFileName, 'rb').read()
image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
msg.attach(image)
	
	
	
#Set up connection and connect to smptp
server = smtplib.SMTP('smtp.gmail.com', 587)
#starttls to encrypt data such as password
server.starttls()
#Login credentials for sender (terminal), server.login(fromaddr, "password")
server.login(fromaddr, "qweQWE1!")
#Define variable for email text                                                                                                                                                                
mailtext = msg.as_string()
#Sends mail
server.sendmail(fromaddr, toaddr, mailtext)
os.remove(ImgFileName)
#Terminates connection
server.quit() 
