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
#Setter filbanen til kaskaden
cascPath = '/home/pi/OSecurity/haarcascade_frontalface_default.xml'
facesFound = ""
#initialiserer kaskaden
faceCascade = cv2.CascadeClassifier(cascPath)
#Setter opp innstillinger for video, fargespekter og oppløsning
rawCapture = PiRGBArray(camera, size=(360, 240))



sleep(1)
#Loop for å ta opp video
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	
	image = frame.array
    #Definere 'gray' som konvertering fra BGR til grayscale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	

	faces = faceCascade.detectMultiScale(
        	gray,
        	scaleFactor=1.1,
        	minNeighbors=5,
        	minSize=(30, 30),
        	flags=cv2.cv.CV_HAAR_SCALE_IMAGE
	)
    #Tegner opp et rektangel der et ansikt er funnet
	for (x, y, w, h) in faces:
        	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
	#Viser frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
	
 
	# Tømmer streamen for å klargjøre for neste frame
	rawCapture.truncate(0)
        sleep (10)
        break

	if key == ord("q"):
		break
#Sett bildeoppløsning
camera.resolution = (640, 480)
#For å få unike filnavn bruker vi timestamp som en variabel når vi lagrer bilder
localtime = time.asctime (time.localtime(time.time()))
# Om systemet f.eks. kjøres for første gang så sjekker vi om pathen eksisterer, hvis ikke lager vi denne mappen
if not os.path.exists('/home/pi/OSecuritySnapshots'):
    os.makedirs('/home/pi/OSecuritySnapshots')
#Åpner kamera preview på terminalen
camera.start_preview()
sleep (2)
camera.capture('/home/pi/OSecuritySnapshots/%s.png' % localtime)
faceImage = ('/home/pi/OSecuritySnapshots/%s.png' % localtime)
imagePath = ('/home/pi/OSecuritySnapshots/%s.png' % localtime)


#Bbilde blir lest ved cv2.imread()
image = cv2.imread(imagePath)
#Setter bilde til gråskala (for begrunnelse ref. ICA06)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#detectMultiScale finner objekter 
faces = faceCascade.detectMultiScale(
    gray,
    #scaleFactor kompanserer for distanser (f.eks. ansikt på et bankkort) og sensitivitet 
    #f.eks. øker man scaleFactor om man den finner ansikt som eksisterer (f.eks. bilde i bakgrunn)
    scaleFactor=1.2,
    #minNeighbors viser til hvor mange objekter som er i nærheten av det originale objektet
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
#Navigerer til den korrekte filbanen og returnerer nåværende arbeidende filbane. Gir nytt navn til fil om ansikt er funnet
os.chdir('/home/pi/OSecuritySnapshots')
os.listdir(os.getcwd())
if facesFound:
        print (faceImage + " " + "renamed to faceFound.png")
        os.rename(faceImage, "faceFound.png")
        extProc = sp.Popen(['python','/home/pi/OSecurity/sendMail.py'])
	status = sp.Popen.poll(extProc) # status none
        
cv2.waitKey(10000)
    

