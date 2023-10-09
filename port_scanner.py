#!/bin/python3 

import sys
import socket
import pyfiglet
import subprocess
from datetime import datetime as dt

subprocess.call('clear', shell=True)
if len(sys.argv)==2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("syntac error. It\'s supposed to be like 192.168.1.x')
    
#adding a banner
print("-"*35)
print("-"*35)
print(pyfiglet.figlet_format("PORT SCANNER"))
print(Scan started at: "+str(dt.now()))
print(f"Starting scan on {target} ")
print("-"*35)
print("-"*35)
 
 #scanner part
 try:
    for port in range(1,65535)
      s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      socket.setdefaulttimeout(1)
      
      #reutrns an error indicator
      result = s.connect_ex((target, port))
      if result ==0
        print("Port {} is open".format(port))
        s.close()
        
except KeyboardInterrupt:
    print("\n Exiting Program!!!)
    sys.exit()
except socket.gaierror:
      print("\n Hostname could not be resolved")
      sys.exit()
except socket.error:
      print("\n Server not responding)
      sys.exit()
