# -*- coding: utf-8 -*-
import time  
import argparse
import shodan
import sys

'''
	[!] Simple python script to get the total number of models indexed in "shodan.io".


	[*] Research: "#stringbleed" (CVE-2017-5135)
		[+] twitter: @stringbleed
		[+] mail to: stringbleed@protonmail.com

		[>] by:
		   [+] Bertin Jose  (Costa Rica) 
		   [+] twitter: @bertinjoseb

		   [+] Fernandez Ezequiel  (Argentina) 
		   [+] twitter: @capitan_alfa

'''

parser = argparse.ArgumentParser(description=' [*] Tool for get the total number of cablemodems vuln to #Stringbleed, (indexed into Shodan)')

parser.add_argument('--models-file', 	dest="MODELS", 	help='select any files with models name of cablemodems')
parser.add_argument('--model',   	 	dest="MODEL", 	help='select any model name')

args        	= parser.parse_args()

allModels      	= args.MODELS
anyModel      	= args.MODEL

class Colors:
    BLUE 		= '\033[94m'
    GREEN 		= '\033[32m'
    RED 		= '\033[0;31m'
    DEFAULT		= '\033[0m'
    ORANGE 		= '\033[33m'
    WHITE 		= '\033[97m'
    BOLD 		= '\033[1m'
    BR_COLOUR 	= '\033[1;37;40m'

query 			= 'MODEL: '
sumTotal 		= [0]

FACETS 			= [
#   	 				('org', 1000),
   						('country', 1000),
#    					('city', 1000)
]

FACET_TITLES = {
#    'org'		: 'Top Organizations',
    'country'	: 'Top Countries',
 #   'city'		: 'Top Cities',
}



					# best harcoded !!!
freeAPIKEY  = 'MM72AkzHXdHpC8iP65VVEEVrJjp7zkgd'
api     	= shodan.Shodan(freeAPIKEY)

# Function search --------------------------------------------------------------------------------------------------- #
def theModelIs(cblMDL):
	#sumTotal 		= 0

	cableModel = str(query+cblMDL)

	result = api.count(cableModel, facets=FACETS)

	print Colors.RED+" # ---------------------------------------------------------------------------- # "
	print Colors.RED+' # '+Colors.GREEN+'  Query:'+Colors.ORANGE+' \t\t\t\" '+cableModel+' \"'
	print Colors.RED+" # ---------------------------------------------------------------------------- # "+Colors.DEFAULT

	totalDevices = result['total']
	print Colors.GREEN+' Total Results: '+Colors.ORANGE+'\t'+str(totalDevices)+Colors.DEFAULT+'\n'
	sumTotal[0] +=  totalDevices

	for facet in result['facets']:
		print " "+Colors.BLUE+str(FACET_TITLES[facet])

		for term in result['facets'][facet]:
			print Colors.GREEN+' %s: %s' % (term['value'], Colors.ORANGE+str(term['count'])+Colors.DEFAULT )

		print ''+Colors.DEFAULT
	time.sleep(2)
	
# ------------------------------------------------------------------------------------------------------------------- #

if (bool(allModels)):
	try:
		cableModels 	= open(allModels,"r")
		#cableModels =

		for model in cableModels:
			md = model[:-1]
			theModelIs(md)
	except Exception, e:
	    print Colors.GREEN+' Error: '+Colors.RED+''+str(e)
	    sys.exit(1)

elif bool(anyModel):
	theModelIs(anyModel)

else:
	print Colors.GREEN+"Select any method of search:"+Colors.ORANGE+" \"--model <model cablemodem> / --models-file <file with models of cablemodems>\""+Colors.DEFAULT
	sys.exit(1)

print "--------------------------------------------------------------------------------- "
if sumTotal[0] > 1000000:
	print Colors.GREEN+"Mas de un millon de Equipos (Indexados) vulnerables a #StringBleed: "+Colors.ORANGE+str(sumTotal[0])+Colors.DEFAULT
else:
	print Colors.GREEN+"[*] Equipos (Indexados) vulnerables a #StringBleed : "+Colors.ORANGE+str(sumTotal[0])+Colors.GREEN
	print "[*] Faltan [ "+Colors.RED+str(1000000 - sumTotal[0])+Colors.GREEN+" ] para llegar al millon"+Colors.DEFAULT
print "--------------------------------------------------------------------------------- "
