import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "Din epost"
toaddr = "cfthorne@hotmail.com"
 
msg = MIMEMultipart()
 
msg['Ricky'] = fromaddr
msg['Christian'] = toaddr
msg['Hei'] = "Tull og fjas"
 
body = "tull"
 
msg.attach(MIMEText(body, 'plain'))
 
 
filename = "hei.txt"
attachment = open("path til fil", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "PASSORD")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()