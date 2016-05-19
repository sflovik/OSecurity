#The server module for the raspberrypi terminal, runs after booting the raspberry pi
#imports for the module
import socket
import subprocess
import os
import time
#Opens the socket connection
soc = socket.socket()        
host = "25.95.63.199"
port = 2004               
soc.bind((host, port))       
soc.listen(5)
#Socket listens, and performs the loop if a connection is established
while 1:
    conn, addr = soc.accept()    
    print ("Got connection from",addr)
    msg = conn.recv(1024).decode()
    print (msg)
    #Recieves message from client application, does something based on variable value

    #First step in arming, if message equals "arming", run the terminalscript
    if ( msg == "arming" ):
        os.system("x-terminal-emulator -e 'bash -c \"python /home/pi/OSecurity/terminalscripts.py; exec bash\"'")
    #If second input from client is "mute", sends key "n" to the terminalscript terminal, muting the buzzer
    elif ( msg == "mute" ):
        subprocess.call(["xdotool", "key", "n"])
        subprocess.call(["xdotool", "key", "Return"])
    #If second input from client is "active", sends key "y" to the terminalscript terminal, activating the buzzer
    elif ( msg == "active"):
         subprocess.call(["xdotool", "key", "y"])
         subprocess.call(["xdotool", "key", "Return"])
    #If message from client equals "disarming", send keyboard-interrupt to terminalscript terminal to disarm the system
    # and send alt+f4 to close the inactive terminal window
    elif ( msg == "disarming"):
         subprocess.call(["xdotool", "key", "ctrl+c"])
         time.sleep(2)
         subprocess.call (["xdotool", "key", "alt+F4"])
    #if input from client does not match any of the presets
    else:
        print ("Invalid input from client...")
