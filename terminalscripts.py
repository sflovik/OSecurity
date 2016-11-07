
#Module for the terminalscript, to be activated on system arming
#Imports for the module, smptp and email for sending email notification
# GPIO for PIR-sensor 
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

#Define the gpio for PIR
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)
muted = ""


	
#Function to start a subprocess and call the buzzermodule script
# If muted variable is true, print confirmation of inactive buzzer
# If the variable isn't true, open a new subprocess with the buzzermodule
def spStart():
	if muted:
		print "The buzzer is inactive/muted in this session"
		extProc = sp.Popen(['python','/home/pi/OSecurity/camera.py'])
		status = sp.Popen.poll(extProc)
		
	else:
		extProc = sp.Popen(['python','/home/pi/OSecurity/buzzermodule.py'])
		status = sp.Popen.poll(extProc) # status none
		extProc2 = sp.Popen(['python','/home/pi/OSecurity/camera.py'])
		status2 = sp.Popen.poll(extProc2) 
		print "Buzzer has been activated!"
		 

#Function to log while system is active, called in the MOTION() function
def writelog():
	localtime = time.asctime (time.localtime(time.time()))
	text_file = open("actlog.txt", "a")
	text_file.write("%s , ble bevegelse oppdaget av PIR detektor og e-post notifikasjon sendt" "\n" "\n" % localtime)
	text_file.close()



#Function to mail an activity log, called on system disarm
def mailactlog():
	fromaddr = "terminalnotificationstation@gmail.com"
	toaddr = "cfthorne@hotmail.com"
 
	msg = MIMEMultipart()
 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "OSecurity - Activity log"
 
	body = "OSecurity is disarmed, activity log since arming is attached"
 
	msg.attach(MIMEText(body, 'plain'))
 
 	#Define filename of attachment and attachments filepath
	filename = "actlog.txt"
	attachment = open('/home/pi/Desktop/actlog.txt' 
	, "rb")
 	#Attaches file to the email
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 	
 	

	msg.attach(part)
 	# Same functionality as sendMail()'s smptp code
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "qweQWE1!")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

#Function to be called on GPIO event, callback
#Calls writelog(), sendMail() and spStart() to, potentially, activate buzzer if it is active
def MOTION (PIR_PIN):
    print "Motion detected by PIR. E-mail notification sent"
    writelog()
    spStart()
    sleep(15)

#Function systemActive() to be called on script startup, listens for gpio-input until KeyboardInterrupt occurs
def systemActive():
	try:
		GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
    		while 1:
        			time.sleep(10)

	except KeyboardInterrupt:
   		print " Quit"
   		print "Disarming OSecurity - sending activity log to registered email"
   		GPIO.cleanup()
		mailactlog()

#On system arming
print "Hi! Would you like the buzzer to be active for this session? y/n"
mute = raw_input ("")
#This is where input from client controls the outcome
#Based on the input the server.py module reads, the server module will either send "y" or "n" to the terminal window

#if local variable mute recieves "y"
if mute == "y":
	print "PIR Module (CTRL+C to exit)"
	time.sleep(2)
	print "Armed with active buzzer"
	#sets global variable "muted" to false, used in spStart()
	muted = False
	systemActive()
#if local variable mute recieves "n"
elif mute == "n":
	print "PIR Module (CTRL+C to exit)"
	time.sleep(2)
	print "Armed with muted buzzer"
	#Sets global variable "muted" to true, used in spStart()
	muted = True
	systemActive()
#if the input is not valid, the seqeuence will be terminated
else:
	print "Invalid input.  Please enter ""y"" for active buzzer or ""n"" for a muted buzzer"
	KeyboardInterrupt
