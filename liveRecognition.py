import cv2
import sys
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
#Dette skriptet er nå implementert i camera.py, utdatert
liveCamera = PiCamera()
liveCamera.resolution = (360, 240)
liveCamera.framerate = 15
liveCamera.rotation = -90
rawCapture = PiRGBArray(camera, size=(360, 240))
cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)
 
# Sleep for å la kamera "varme opp" og starte
time.sleep(0.1)
 
# Ta frames fra kamera i en loop
for frame in liveCamera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	
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
	# Viser frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
	
 
	# Tøm streamen for å klargjøre for neste frame
	rawCapture.truncate(0)
 
	if key == ord("q"):
		break
