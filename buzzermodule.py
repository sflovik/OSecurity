import RPi.GPIO as GPIO
import time

BeepPin = 0

def setup():
	GPIO.setmode(GPIO.BOARD) 
	GPIO.setup(BeepPin, GPIO.OUT)
	GPIO.output(BeepPin, GPIO.HIGH)

def loop():
	while True:
		GPIO.output(BeepPin, GPIO.LOW)

def destroy():
	GPIO.output(BeepPin, GPIO.HIGH) 
	GPIO.cleanup() 

	if __name__ == '__main__': 
		print 'Press Ctrl+C to exit'
setup()
try:
	loop()
except KeyboardInterrupt: 
	destroy()