import cv2
import sys
from picamera import PiCamera
from picamera.array import PiRGBArray
import time

liveCamera = PiCamera()
liveCamera.resolution = (360, 240)
liveCamera.framerate = 15
liveCamera.rotation = -90
rawCapture = PiRGBArray(camera, size=(360, 240))
cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
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
	# show the frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
	
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	if key == ord("q"):
		break
