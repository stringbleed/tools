# fuzzing; Community String
## Simple python script for fuzzer the field "community strings"

# Quick start

* usr@pwn:~$ git clone https://github.com/stringbleed/tools.git
* usr@pwn:~$ cd community_fuzz



# Usage:
	fuzzCommStr-v1.py <host> <version> <community> <community x N> 

## screenshot:
	![community fuzz](https://raw.githubusercontent.com/stringbleed/tools/master/community_fuzz/tool.png)


# Demo:
	''' 
	usr@pwn:~$ python fuzzCommStr-v1.py 192.168.0.1 1 A 50

	exec: snmpget -v 1 -c AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA 192.168.0.1 iso.3.6.1.2.1.1.1.0 

	length injection: 50
	Max injection is: 256

	Start...

	iso.3.6.1.2.1.1.1.0 = STRING: "Cisco DPC3928SL DOCSIS 3.0 1-PORT Voice Gateway <<HW_REV: 1.0; VENDOR: Technicolor; BOOTR: 2.4.0; SW_REV: D3928SL-PSIP-13-A010-c3420r55105-160428a; MODEL: DPC3928SL>>"


	'''

