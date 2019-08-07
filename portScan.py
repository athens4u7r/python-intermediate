from threading import Thread
from socket import *
import optparse

def portScan(tgtHost, tgtPorts):
  try:
    tgtIP = gethostbyname(tgtHost)
  except:
    print("Could not resolve host")
    return
  try:
    

def main():
  parser = optparse.OptionParse("usage %prog -H <hostname> -p <port number(s)>")
  parser.add_option("-H", dest= "tgtHost", type= "string", help= "specify the hostname")
  parser.add_option("-p", dest= "tgtPort", type= "string", help= "specify the port number(s)")
  
  (options, args) = parser.parse_args()
  
  tgtHost = options.tgtHost
  tgtPorts = str(options.tgtPort).split(',')
  
  if tgtHost == None and tgtPorts[0] == None:
    print(parser.usage)
    exit(0)
  portScan(tgtHost, tgtPorts)
 
