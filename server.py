import socket
import subprocess
import os
import time
soc = socket.socket()        
host = "25.95.63.199"
port = 2004               
soc.bind((host, port))       
soc.listen(5)
while 1:
    conn, addr = soc.accept()    
    print ("Got connection from",addr)
    msg = conn.recv(1024).decode()
    print (msg)
    if ( msg == "arming" ):
        os.system("x-terminal-emulator -e 'bash -c \"python /home/pi/OSecurity/terminalscripts.py; exec bash\"'")
    elif ( msg == "mute" ):
        subprocess.call(["xdotool", "key", "n"])
        subprocess.call(["xdotool", "key", "Return"])
       
    elif ( msg == "active"):
         subprocess.call(["xdotool", "key", "y"])
         subprocess.call(["xdotool", "key", "Return"])
    elif ( msg == "disarming"):
         subprocess.call(["xdotool", "key", "ctrl+c"])
         time.sleep(2)
         subprocess.call (["xdotool", "key", "alt+F4"])
    else:
        print ("Invalid input from client...")
