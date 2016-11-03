from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = -90
camera.start_preview()

sleep(15)
camera.stop_preview()