#Coded By B3mB4m
#Concat : b3mb4m@protonmail.com

from utils import *


def bochs_reg_key1():
	return pyfish_exists_regkey_value_str(HKEY_LOCAL_MACHINE, "HARDWARE\\Description\\System", "SystemBiosVersion", "BOCHS");

#int bochs_cpu_amd1() {}
#int bochs_cpu_amd2() {}
#int bochs_cpu_intel1() {}