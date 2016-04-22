import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import time

def writelog():
	localtime = time.asctime (time.localtime(time.time()))
	text_file = open("actlog.txt", "a")
	text_file.write("%s , ble bevegelse oppdaget av PIR detektor og e-post notifikasjon sendt" "\n" "\n" % localtime)
	text_file.close()

def sendmail():
	#Definere variabler for sender og mottaker
	fromaddr = "sondrf14@gmail.com"
	toaddr = "cfthorne@hotmail.com"

	msg = MIMEMultipart()
	#Sette avsender
	msg['From'] = fromaddr
	#Sette mottaker
	msg['To'] = toaddr
	#Sette emne for epost
	msg ['Subject'] = "Bevegelse oppdaget - alarm"
	#Definere variabel med epostens tekst
	body = "Bevegelsessensoren har oppdaget anomaliteter."
	msg.attach(MIMEText(body, 'plain'))

	#Sett opp og koble til smptp 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	#starttls for beskyttelse av passord
	server.starttls()
	#Innloggingskredentialene for valgt smptp
	server.login("sondrf14@gmail.com", "rtyRTY1!")
	#Definere variabel for mailens tekst                                                                                                                                                                     
	mailtext = msg.as_string()
	#Sender mailen med angitte variabler
	server.sendmail(fromaddr, toaddr, mailtext)
	#Stopper koblingen
	server.quit()   

def mailactlog():
	fromaddr = "sondrf14@gmail.com"
	toaddr = "cfthorne@hotmail.com"
 
	msg = MIMEMultipart()
 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Aktivitetslogg"
 
	body = "Aktivitetslogg siste dag"
 
	msg.attach(MIMEText(body, 'plain'))
 
 
	filename = "actlog.txt"
	attachment = open('/home/linux/OSecurity/actlog.txt' 
	, "rb")
 
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
	msg.attach(part)
 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "rtyRTY1!")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
writelog()
sendmail()
mailactlog()