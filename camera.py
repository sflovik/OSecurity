from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep
import time
import os
import smtplib
import RPi.GPIO as GPIO
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import subprocess as sp
import cv2
import sys

camera = PiCamera()
camera.rotation = -90
camera.resolution = (360, 240)
camera.framerate = 32

faceImage = ""
cascPath = '/home/pi/OSecurity/haarcascade_frontalface_default.xml'
facesFound = ""
faceCascade = cv2.CascadeClassifier(cascPath)
rawCapture = PiRGBArray(camera, size=(360, 240))


#for i in range(1):
sleep(1)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	
	image = frame.array
 
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
	faces = faceCascade.detectMultiScale(
        	gray,
        	scaleFactor=1.1,
        	minNeighbors=5,
        	minSize=(30, 30),
        	flags=cv2.cv.CV_HAAR_SCALE_IMAGE
	)
	for (x, y, w, h) in faces:
        	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
	# show the frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
	
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
        sleep (10)
        break

	if key == ord("q"):
		break

camera.resolution = (640, 480)
localtime = time.asctime (time.localtime(time.time()))
if not os.path.exists('/home/pi/OSecuritySnapshots'):
    os.makedirs('/home/pi/OSecuritySnapshots')
camera.start_preview()
sleep (2)
camera.capture('/home/pi/OSecuritySnapshots/%s.png' % localtime)
faceImage = ('/home/pi/OSecuritySnapshots/%s.png' % localtime)
imagePath = ('/home/pi/OSecuritySnapshots/%s.png' % localtime)



image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
print "Found {0} faces".format(len(faces))
camera.stop_preview()
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    facesFound = True
    cv2.imshow("Faces found" ,image)
os.chdir('/home/pi/OSecuritySnapshots')
os.listdir(os.getcwd())
if facesFound:
        print (faceImage + " " + "renamed to faceFound.png")
        os.rename(faceImage, "faceFound.png")
        extProc = sp.Popen(['python','/home/pi/OSecurity/sendMail.py'])
	status = sp.Popen.poll(extProc) # status none
        
cv2.waitKey(10000)
    #cv2.destroyAllWindows()
    #i+=1

