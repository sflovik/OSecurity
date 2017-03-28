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

GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)
action = ""

processID = 1
pid = os.getpid()
#print(str(pid)) returns 4375




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

activeThread = myThread(processID, "System Active Thread")

mqtt_client = mqtt.Client(client_id="osecpi", clean_session=True)
def writelog():
	localtime = time.asctime (time.localtime(time.time()))
	text_file = open("actlog.txt", "a")
	text_file.write("%s , ble bevegelse oppdaget av PIR detektor og e-post notifikasjon sendt" "\n" "\n" % localtime)
	text_file.close()



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


def MOTION (PIR_PIN):
    print ("Motion detected by PIR. E-mail notification sent")
    writelog()
    #spStart()
    sleep(15)

#Function systemActive() to be called on script startup, listens for gpio-input until KeyboardInterrupt occurs
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



#Dette er subscribe client 
#Den skal"subcribe" til en topic paa MQTT broker, AWS
#App skal altsaa oppdatere broker med en beskjed paa en topic
#Videre skal subcriberen paa raspberry utfore handling basert paa payload fra broker

def on_message (mqttc, obj, msg):
    global message
    #print(msg.topic + " " + str(msg.qos) + "  " + str(msg.payload))
    message = msg.payload.decode()
    
    
    if message == "y":
        print(processID)
        print("arming")
        action = "armed"
        mqtt_client.publish("/osecurity/fromterminal", action)
        #TODO start sub-process for aktivering
        #extProc = sp.Popen(['python','/home/pi/OSecurity/pahoTest.py'])
        #extProc.systemActive() --> AttributeError: 'Popen' object has no attribute 'systemActive'
        #if processID == 2:
        #    activeThread = myThread(processID, "System Active Thread")
        #    print("starting second process with processID: " + str(processID))
        #    activeThread.start()
        #elif processID > 1:
        #    activeThread = myThread(processID, "System Active Thread")
        #    print("starting third process with processID: " + str(processID))
        global activeThread
        activeThread = myThread(processID, "System Active Thread")
        activeThread.start()

         
    elif message == "n":
        action = "disarmed"
        print(str(pid))
        mqtt_client.publish("/osecurity/fromterminal", action)
        print("disarming")
        #TODO stopp sub-process
        #extProc.terminate()
        activeThread.terminate()
        
def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))
    mqttc.publish("/osecurity/fromtermianl", action)
    
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


mqtt_client.tls_set("/home/pi/Downloads/AWS/root-CA.crt",certfile="/home/pi/Downloads/AWS/OSEC-TERMINAL.cert.pem",
                    keyfile="/home/pi/Downloads/AWS/OSEC-TERMINAL.private.key",
                    tls_version=ssl.PROTOCOL_TLSv1_2,ciphers=None)

mqtt_client.connect("a3enni6esrlrke.iot.eu-west-1.amazonaws.com", port=8883)



mqtt_client.loop_forever()



