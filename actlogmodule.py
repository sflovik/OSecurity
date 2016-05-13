import time

localtime = time.asctime (time.localtime(time.time()))
text_file = open("actlog.txt", "a")
text_file.write("%s , ble bevegelse oppdaget av PIR detektor og e-post notifikasjon sendt" "\n" "\n" % localtime)
text_file.close()