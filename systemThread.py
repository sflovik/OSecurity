import time
import threading
import pahoTest



class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        pahoTest.systemActive()
    def killThread():
        activeThread.exit()




# Create new thread
activeThread = myThread(1, "System Active Thread", 1)


# Start the new thread
activeThread.start()
