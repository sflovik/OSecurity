#Buzzer module for the terminal

#imports time and GPIO
import RPi.GPIO as GPIO
import time

#Define the gpio-pin that the buzzer is connected to
BeepPin = 18

#function to set up the GPIO settings
def setup():
	GPIO.setmode(GPIO.BOARD) 
	GPIO.setup(BeepPin, GPIO.OUT)
	GPIO.output(BeepPin, GPIO.HIGH)

#function loop to run when script is called, sends high / low output to create beeping on buzzer
def loop():
	while True:
		GPIO.output(BeepPin, GPIO.LOW)
		time.sleep(0.5)
		GPIO.output(BeepPin, GPIO.HIGH)
		time.sleep(0.5)
#Function to terminate the GPIO and stop everything, called on KeyboardInterrupt
def destroy():
	GPIO.output(BeepPin, GPIO.HIGH) 
	GPIO.cleanup() 

	if __name__ == '__main__': 
		print 'Buzzer has been deactivated'
setup()
try:
	loop()
except KeyboardInterrupt: 
	destroy()