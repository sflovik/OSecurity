#Imports
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
#Definere variabler for sender og mottaker
fromaddr = "avsender@epost.com"
toaddr = "mottaker@epost.com"

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
server.login("avsender@epost.com", "passord")
#Definere variabel for mailens tekst                                                                                                                                                                     
mailtext = msg.as_string()
#Sender mailen med angitte variabler
server.sendmail(fromaddr, toaddr, mailtext)
#Stopper koblingen
server.quit()                       
