from picamera import PiCamera
from time import sleep
import time
import os

localtime = time.asctime (time.localtime(time.time()))

camera = PiCamera()
camera.rotation = -90
camera.start_preview()
sleep(5)
for i in range(5):
    sleep(1)
    if not os.path.exists('/home/pi/OSecuritySnapshots'):
        os.makedirs('/home/pi/OSecuritySnapshots')
    camera.capture('/home/pi/OSecuritySnapshots/%s.jpg' % localtime)
camera.stop_preview()
