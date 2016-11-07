import cv2
import sys
import os

#user values
imagePath = '/home/pi/OSecurity/testimage.jpg'
cascPath = '/home/pi/OSecurity/haarcascade_frontalface_default.xml'
facesFound = ""
faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
	gray,
	scaleFactor=1.1,
	minNeighbors=5,
	minSize=(30, 30),
	flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)
print "Found {0} faces".format(len(faces))

for (x, y, w, h) in faces:
	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
	facesFound = True

cv2.imshow("Faces found" ,image)
os.listdir(os.getcwd())
if facesFound:
        os.rename("testimage.jpg", "facefound.jpg")
cv2.waitKey(0)
