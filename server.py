import socket
import subprocess
import os
soc = socket.socket()        
host = "25.53.39.221"
port = 2004               
soc.bind((host, port))       
soc.listen(5)
os.system("gnome-terminal -e 'bash -c \"python terminalscripts.py; exec bash\"'")
while 1:
    conn, addr = soc.accept()    
    print ("Got connection from",addr)
    msg = conn.recv(1024).decode()
    print (msg)
    if ( msg == "mute" ):
        subprocess.call([xdotool], "key", ["n"])
        subprocess.call(["xdotool", "key", "Return"])
       
    elif ( msg == "active"):
         subprocess.call(["xdotool", "key", "y"])
         subprocess.call(["xdotool", "key", "Return"])
    else:
        print ("Invalid input from client...")
