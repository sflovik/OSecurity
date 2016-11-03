from picamera import PiCamera
from time import sleep
import time
import os


camera = PiCamera()
camera.rotation = -90
camera.start_preview()
sleep(5)
for i in range(5):
    sleep(1)
    localtime = time.asctime (time.localtime(time.time()))
    if not os.path.exists('/home/pi/OSecuritySnapshots'):
        os.makedirs('/home/pi/OSecuritySnapshots')
    camera.capture('/home/pi/OSecuritySnapshots/%s.jpg' % localtime)
    i+=1
camera.stop_preview()
