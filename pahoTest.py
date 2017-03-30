import os
import paho.mqtt.client as mqtt
import ssl
import subprocess as sp
import smtplib
import os
import RPi.GPIO as GPIO
import email.mime.base
import time
import threading
import systemThread
import multiprocessing
import psutil
from time import sleep
from picamera import PiCamera
import boto
import boto3
from boto.s3.key import Key
from datetime import datetime
from threading import Timer


GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)
action = ""
localtime = time.asctime (time.localtime(time.time()))





client = boto3.client('sns', region_name='eu-west-1')
s3 = boto.connect_s3()

processID = 1
processID2 = 1
processID3 = 1

pid = os.getpid()
#print(str(pid)) returns 4375

class TaskThread(multiprocessing.Process):
    """Thread that executes a task every N seconds"""
    
    def __init__(self, processID, name):
        multiprocessing.Process.__init__(self)
        self.processID = processID3
        self.name = name
        self._finished = threading.Event()
        self._interval = 15.0
    
    def setInterval(self, interval):
        """Set the number of seconds we sleep between executing our task"""
        self._interval = interval
    
    def shutdown(self):
        """Stop this thread"""
        self._finished.set()
    
    def run(self):
        while 1:
            if self._finished.isSet(): return
            self.task()
            
            # sleep for interval or until shutdown
            self._finished.wait(self._interval)
    
    def task(self):
        snapshot()
        boto.set_stream_logger('boto')
        bucket = s3.get_bucket('latest-snapshot', validate=False)
        exists = s3.lookup('latest-snapshot')
        for bucket in s3:
           for key in bucket:
               print(key.name)
        key = s3.get_bucket('latest-snapshot').get_key('ic_menu.png')
        key.set_contents_from_filename('/home/pi/OSecuritySnapshots/latestSnapshot.png')
    #key.get_contents_to_filename('/home/pi/s3download.jpg')
        pass


class myThread (multiprocessing.Process):
    def __init__(self, processID, name):
        multiprocessing.Process.__init__(self)
        self.processID = processID
        self.name = name
    def run(self):
        print "Starting " + self.name
        global processID
        processID += 1
        systemActive()

def killThread():
        activeThread.terminate() 
def killS3Thread():
        s3Thread.terminate()
        
activeThread = myThread(processID, "System Active Thread")
s3Thread = myThread(processID2, "S3 thread active")
timeThread = TaskThread(processID3, "Time thread active")
    
mqtt_client = mqtt.Client(client_id="osecpi", clean_session=True)
def writelog():
	localtime = time.asctime (time.localtime(time.time()))
	text_file = open("actlog.txt", "a")
	text_file.write("%s , ble bevegelse oppdaget av PIR detektor og e-post notifikasjon sendt" "\n" "\n" % localtime)
	text_file.close()

def snapshot():
    if not os.path.exists('/home/pi/OSecuritySnapshots'):
        os.makedirs('/home/pi/OSecuritySnapshots')
    camera = PiCamera()
    camera.rotation = -90
    camera.start_preview()
    sleep (3)
    camera.capture('/home/pi/OSecuritySnapshots/latestSnapshot.png')
    camera.stop_preview()
    camera.close()

def camera():
    if not os.path.exists('/home/pi/OSecurityNotifications'):
        os.makedirs('/home/pi/OSecurityNotifications')
    camera = PiCamera()
    camera.rotation = -90
    localtime = time.asctime (time.localtime(time.time()))
    
    camera.start_preview()
    sleep (3)
    camera.start_recording('/home/pi/OSecurityNotifications/%s.h264' % localtime)
    sleep(10)
    camera.stop_recording()
    camera.capture('/home/pi/OSecurityNotifications/%s.png' % localtime)
    camera.stop_preview()
    camera.close()

#Function to mail an activity log, called on system disarm
def mailactlog():
	fromaddr = "terminalnotificationstation@gmail.com"
	toaddr = "cfthorne@hotmail.com"
 
	msg = MIMEMultipart()
 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "OSecurity - Activity log"
 
	body = "OSecurity is disarmed, activity log since arming is attached"
 
	msg.attach(MIMEText(body, 'plain'))
 
 	#Define filename of attachment and attachments filepath
	filename = "actlog.txt"
	attachment = open('/home/pi/Desktop/actlog.txt' 
	, "rb")
 	#Attaches file to the email
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 	
 	

	msg.attach(part)
 	# Same functionality as sendMail()'s smptp code
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "qweQWE1!")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	
def S3Test():
    boto.set_stream_logger('boto')
    bucket = s3.get_bucket('latest-snapshot', validate=False)
    exists = s3.lookup('latest-snapshot')
    for bucket in s3:
       for key in bucket:
           print(key.name)
    
    key = s3.get_bucket('latest-snapshot').get_key('ic_menu.png')
    key.set_contents_from_filename('/home/pi/OSecuritySnapshots/latestSnapshot.png')
    #key.get_contents_to_filename('/home/pi/s3download.jpg')
   
    
def timedTask():
    global s3Thread
    s3Thread = myThread(processID2, "S3 thread active")
    s3Thread.start()
    S3Test()
    sleep(5)
    killS3Thread()
    
def MOTION (PIR_PIN):
    print ("Motion detected by PIR. E-mail notification sent")
    camera()
    writelog()
    camera()
    sleep(5)
 


def systemActive():
        try:
                GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
           
                while 1:
                        time.sleep(10)

        except KeyboardInterrupt:
                 print (" Quit")
                 print ("Disarming OSecurity - sending activity log to registered email")
                 GPIO.cleanup()
                 #mailactlog()





def on_message (mqttc, obj, msg):
    global message
    message = msg.payload.decode()
    
    
    if message == "y":
        print("arming")
        action = "armed"
        mqtt_client.publish("/osecurity/fromterminal", action)

        global activeThread
        activeThread = myThread(processID, "System Active Thread")
        activeThread.start()

         
    elif message == "n":
        action = "disarmed"
        mqtt_client.publish("/osecurity/fromterminal", action)
        print("disarming")
        activeThread.terminate()
        
def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))
    mqttc.publish("/osecurity/fromterminal", action)
    
def on_connect (mqttc, obj, flags, rc):
    mqttc.subscribe("/osecurity/fromapp", 0)
    if rc==0:
        print ("HALLA, successful")
        
    
def on_subscribe (mqttc, obj, mid, granted_qos):
    print ("Subscribed: " + str(mid) + " " + str(granted_qos))
    mqtt_client.publish ("/osecurity/fromterminal", "Terminal er online")

mqtt_client.on_subscribe = on_subscribe    
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message


global timeThread
timeThread = TaskThread(processID3, "S3 thread/proocess active")
timeThread.start()
         


mqtt_client.tls_set("/home/pi/Downloads/AWS/root-CA.crt",certfile="/home/pi/Downloads/AWS/OSEC-TERMINAL.cert.pem",
                    keyfile="/home/pi/Downloads/AWS/OSEC-TERMINAL.private.key",
                    tls_version=ssl.PROTOCOL_TLSv1_2,ciphers=None)

mqtt_client.connect("a3enni6esrlrke.iot.eu-west-1.amazonaws.com", port=8883)



mqtt_client.loop_forever()





