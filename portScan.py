# PORT SCANNER
# FILTERED PORTS ARE CONSIDERED CLOSED
# AUTHOR => P0531D0N
# MOOD => DONO

from socket import *
import optparse
from threading import Thread

def connScan(tgtHost, tgtPort):
	try:
		skt = socket(AF_INET, SOCK_STREAM)
		skt.connect((tgtHost, tgtPort))
		skt.send("This is Ndimz\r\n")
		results = skt.recv(100)

		print("%s/tcp open" % (tgtPort))
		print(str(results))
	except:
		print("%s/tcp closed" % (tgtPort))
	finally:
		skt.close()

def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print('Host could not be resolved: Unknown: %s' % tgtHost)
		return
	try:
		tgtName = gethostbyaddr(tgtIP)
		print('Scan results for %s' % (tgtName))
	except:
		print('Scan results for %s' % (tgtIP))

	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan,args=(tgtHost, int(tgtPort)))
		t.start()

def main():
	parser = optparse.OptionParser('usage %prog -H <hostname> -p <port(s)>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify hostname')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify port(s)')

	(options, args) = parser.parse_args()

	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')

	if (tgtHost == None) or (tgtPorts[0] == None):
		print(parser.usage)
		exit(0)
	portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
	main()
