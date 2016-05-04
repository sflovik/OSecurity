import RPi.GPIO as GPIO
import time

BeepPin = 11

def setup():
	GPIO.setmode(GPIO.BOARD) 
	GPIO.setup(BeepPin, GPIO.OUT)
	GPIO.output(BeepPin, GPIO.HIGH)

def loop():
	while True:
		GPIO.output(BeepPin, GPIO.LOW)
		time.sleep(1)
		GPIO.output(BeepPin, GPIO.HIGH)
		time.sleep(1)

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