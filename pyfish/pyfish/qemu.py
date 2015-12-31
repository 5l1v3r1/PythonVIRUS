#Coded By B3mB4m
#Concat : b3mb4m@protonmail.com

from utils import *



def qemu_reg_key1():
	return pyfish_exists_regkey_value_str(HKEY_LOCAL_MACHINE, "HARDWARE\\DEVICEMAP\\Scsi\\Scsi Port 0\\Scsi Bus 0\\Target Id 0\\Logical Unit Id 0", "Identifier", "QEMU");


def qemu_reg_key2():
	return pyfish_exists_regkey_value_str(HKEY_LOCAL_MACHINE, "HARDWARE\\Description\\System", "SystemBiosVersion", "QEMU");



#int qemu_cpu_name() {}
