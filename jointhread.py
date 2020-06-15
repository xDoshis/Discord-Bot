import threading
import time
import ftplib

exitFlag = 0

class FTP (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      print ("Starting " + self.name)
      ftp_call(self.name, 2, self.counter)
      print ("Exiting " + self.name)

def ftp_call(threadName, counter, delay):
    join_old = 0
    while counter:
        if exitFlag:
            threadName.exit()
        #Open ftp connection
        ftp = ftplib.FTP('***', '***','***') #FTP login goes here

        #Get the readme file for Join
        ftp.cwd("/plugins/ServerLog/Activity/Player Join")
        File = open("join.txt", "wb")
        ftp.retrbinary('RETR '+ftp.nlst()[0], File.write)
        File.close()
      
        ftp.close()
        
        #parse join file contents into lines 
        File = open("join.txt", "r")
        jsonLineJ = File.readlines()
        File.close()

        join_new = len(jsonLineJ)

        print("\n These players have **JOINED**")

        if join_new == join_old:
            print("No new players have joined.")

        if join_new > join_old:
            loggedin = join_new - join_old
            i = 1
            while i <= loggedin:
                print(jsonLineJ[-i])
                i = i +1
            join_old = join_new
    
        if join_new < join_old:
            for element in jsonLineJ:
                print(jsonLineJ[element])
            join_old = join_new 

      #print "%s: %s" % (threadName, time.ctime(time.time())
        time.sleep(delay)

        # ***KILLING THE THREAD***
        counter = counter -1


# Create new threads
thread1 = FTP(1, "Thread-1", 1)
# Start new Threads
thread1.start()
print ("Exiting Main Thread")