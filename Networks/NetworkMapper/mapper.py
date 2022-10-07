from socket import *
import time

def serviceMapper():
    pass

def osInfo():
    pass

def vulnScanner():
    pass

def spoofDevice():
    pass

def portScan():
   startTime = time.time()

   target = input('Enter the host to be scanned: ')
   t_IP = gethostbyname(target)
   start, end = eval(input("Enter port range( start, stop): "))
   print ('Starting scan on host: ', t_IP)

   for i in range(start, end+1):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
         print ('Port %d: OPEN' % (i,))
      s.close()
   print('Time taken:', time.time() - startTime)

portScan()
