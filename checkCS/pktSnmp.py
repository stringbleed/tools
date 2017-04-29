# -*- coding: utf-8 -*- 
# Lib SNMP version 0.1

import random
dataType = {
				'primitive': {
								'Integer'			: '0x02', #
								'OctetString'		: '0x04', #
								'Null'				: '0x05', #
								'ObjectIdentifier'	: '0x06', #
				},
				'complex': {
								'Secuence'			: '0x30', # 
								'GetRequest'		: '0xa0', #
								'GetResponse' 		: '0xa2', #
								'SetRequest'	 	: '0xa3', #
				}
}

def ranRqsID():
	isRandom = str(hex(random.randrange(268435456,4294967295))[2:])
	return isRandom

chrX = ""

fullPaket 	= [
		# 														INDEX LIST :
		#      													     ||
		# ------------------------------------------------------------------------------------------------------------- #
		# -- 'Header' SNMP --- 										 \/										  			#
		# ------------------------------------------------------------------------------------------------------------- #
		# _1_ SNMP -- MESSAGE
					dataType['complex']['Secuence'][2:], 			# 0# Type 		- 	Secuence
					'LL', 											# 1# Length 	- 	Function --> CALC length HERE
		# _2_ SNMP -- VERSION 
					dataType['primitive']['Integer'][2:], 			# 2# Type 		- 	Integer
					'01', 											# 3# Length 	- 	01         
					'00', 											# 4# Version   	- 	IF '00' = SNMP_v1 || IF '01' = SNMP_v2
		# _3_ SNMP -- COMMUNITY STRING
					dataType['primitive']['OctetString'][2:],		# 5# Type 		- 	Octect String
					'iLenCommunity',								# 6# Length 	- 	0a 	
					'iStrCommunity', 								# 7# Comm str 	- 	Hardcoded: 'insecurity'

		# ------------------------------------------------------------------------------------------------------------- #
		# -- Start PDU --- 																					  			#
		# ------------------------------------------------------------------------------------------------------------- #

		# _4_ SNMP -- PDU 
					dataType['complex']['GetRequest'][2:], 			# 8# Type 		- 	GetRequest
					'LL', 											# 9# Length 	-   Function --> CALC length HERE
		# _5_ SNMP -- REQUEST ID 
					dataType['primitive']['Integer'][2:], 			#10# Type 		- 	Integer
					'04', 											#11# Length 	- 	04 
					ranRqsID(), 									#12# Trans ID 	- 	Random generation  
		# _6_ SNMP -- ERROR
					dataType['primitive']['Integer'][2:], 			#13# Type 		- 	Integer
					'01', 											#14# Length 	- 	01 
					'00', 											#15# Value 		- 	00
		# _7_ SNMP -- ERROR INDEX -
					dataType['primitive']['Integer'][2:], 			#16# Type 		- 	Integer
					'01', 											#17# Length 	- 	01 
					'00', 											#18# Value 		- 	00
		# _8_ SNMP -- VARBIND LIST
					dataType['complex']['Secuence'][2:], 			#19# Type 		- 	Secuence
					'LL', 											#20# Length 	-   Function --> CALC length HERE
		# _9_ SNMP -- VARBIND
					dataType['complex']['Secuence'][2:], 			#21# Type 		- 	Secuence
					'LL', 											#22# Length 	-   Function --> CALC length HERE
		# _10_ SNMP -- OBJECT IDENTIFIER
					dataType['primitive']['ObjectIdentifier'][2:], 	#23# Type 		- 	Object Identifier
					'L_OID', 										#24# Length 	-   Only length OID
					'isOid', 										#25# OID
		# _11_ SNMP -- 
					dataType['primitive']['Null'][2:], 				#26# Type 		- 	Null
					'00' 											#27# Value 		- 	00
	]

# ej Community
# 696e7365637572697479
#  pkt_03_index('696e7365637572697479')
def pkt_03_index(comm):
	lengthComm 		= str(hex(len(comm) / 2)[2:]).zfill(2)
	
	fullPaket[6] 	= lengthComm
	fullPaket[7] 	= comm

# ej OID
# 2b06010401a30b0204010106010100
# pkt_10_index('2b06010401a30b0204010106010100')
def pkt_10_index(finalOID):
	lengthOID 		= str(hex(len(finalOID) / 2)[2:]).zfill(2)
	fullPaket[24] 	= lengthOID
	fullPaket[25] 	= finalOID

def getLenghts(iLen):
	chrX = ""
	cntIndx = (int(iLen)+1)
	retLen = str(hex(len(chrX.join(fullPaket[cntIndx:]))/ 2 )[2:]).zfill(2)
	chrX = ""
	return retLen

def setLengths():
	fullPaket[22] 	= getLenghts(22)
	fullPaket[20] 	= getLenghts(20)
	fullPaket[9] 	= getLenghts(9)
	fullPaket[1] 	= getLenghts(1)

def getFUllPkt(initOid,initComm):
	pkt_03_index(initComm)
	pkt_10_index(initOid)
	setLengths()

	chrX = ""
	fullFrame = chrX.join(fullPaket)
	return fullFrame