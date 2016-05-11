import socket
import win32com.client as comclt
soc = socket.socket()        
host = "25.31.197.199"
port = 2004               
soc.bind((host, port))       
soc.listen(5)
#os.system("gnome-terminal -e 'bash -c \"python terminalscripts.py; exec bash\"'")
while 1:
    conn, addr = soc.accept()    
    print ("Got connection from",addr)
    msg = conn.recv(1024).decode()
    print (msg)
    if ( msg == "mute" ):
        wsh = comclt.Dispatch("WScript.Shell")
        wsh.SendKeys("n")
        wsh.SendKeys("{ENTER}")
    elif ( msg == "active"):
        wsh = comclt.Dispatch("WScript.Shell")
        wsh.SendKeys("y")
        wsh.SendKeys("{ENTER}")
    else:
        print ("Invalid input from client...")
