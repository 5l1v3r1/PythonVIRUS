import pefile
import re
import sys

#Coded by B3mB4m
#That script find max injectable code cave leghth for you.

def CClength( exe):
	pe = pefile.PE( exe)
	db = ""
	for x in pe.sections:
		db += x.get_data().encode("hex")
	cache = re.findall("..?", db)

	cout = 0
	maxtotal = 0
	for x in cache:
		if x == "00":
			cout += 1
			maxtotal = cout
		else:
			cout = 0
	return maxtotal


if __name__ == '__main__':
	print ("\nMaximum code cove size :  {0} \n").format(CClength( sys.argv[1]))