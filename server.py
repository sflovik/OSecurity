import socket              
soc = socket.socket()        
host = "192.168.137.131"
port = 2004               
soc.bind((host, port))       
soc.listen(5)               
while True:
    conn, addr = soc.accept()    
    print ("Got connection from",addr)
    msg = conn.recv(1024)
    print (msg)
if ( msg == "Hello Server" ):
    print("Hii everyone")
else:
    print("Go away")