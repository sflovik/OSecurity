import RPi.GPIO as GPIO
import time

BeepPin = 18

def setup():
	GPIO.setmode(GPIO.BOARD) 
	GPIO.setup(BeepPin, GPIO.OUT)
	GPIO.output(BeepPin, GPIO.HIGH)

def loop():
	while True:
		GPIO.output(BeepPin, GPIO.LOW)
		time.sleep(0.5)
		GPIO.output(BeepPin, GPIO.HIGH)
		time.sleep(0.5)

def destroy():
	GPIO.output(BeepPin, GPIO.HIGH) 
	GPIO.cleanup() 

	if __name__ == '__main__': 
		print 'Press Ctrl+C again to stop the buzzer'
setup()
try:
	loop()
except KeyboardInterrupt: 
	destroy()