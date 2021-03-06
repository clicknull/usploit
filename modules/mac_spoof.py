#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import sys
import os
from core import colors
from collections import OrderedDict
from scapy.all import *
from core import network_scanner
import random
from core import getpath
from core.setvar import setvar

# Info about the module
# Module's name (should be same as file's name)
name = "mac_spoof"
# Module version
version = "1.0"
# Description
desc = "mac spoof"
# Creator's github
github = "4shadoww"
# Creator's name
createdby = "4shadoww"
# Email
email = "4shadoww0@gmail.com"
# Alert user if root permissions not available (remove variable below if root permissions not needed)
needroot = 1

#custom commands
customcommands = (
'scan',
'random_mac',
'reset',
)

# List of the variables
variables = OrderedDict((
('fake_mac', '02:a0:04:d3:00:11'),
('interface', 'eth0'),
))

# Description for variables
vdesc = [
'fake mac',
'network interface',
]

mhelp =  OrderedDict((
('scan', 'scan network'),
('random_mac', 'generate random mac'),
('reset', 'end mac spoof'),
))

# Additional help notes
help_notes = colors.red+"this module will not work without root permissions!"+colors.end

# Additional notes to options
option_notes = colors.yellow+" you can generate fake_mac using 'random_mac' command\n use 'reset' command to end mac spoof"+colors.end

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	xterm1 = "service network-manager stop"
	xterm2 = "ifconfig "+variables['interface']+" hw ether "+variables['fake_mac']
	xterm3 = "service network-manager start"
	print(colors.blue+"[*] starting mac spoof"+colors.yellow)
	os.system(xterm1)
	print(colors.green+"trying to set fake mac address..."+colors.yellow)
	os.system(xterm2)
	os.system(xterm3)
	print(colors.green+"done!"+colors.end)

def scan():
	network_scanner.scan()

def random_mac():
	mac = "f4:ac:c1:%02x:%02x:%02x" % (
		random.randint(0, 255),
		random.randint(0, 255),
		random.randint(0, 255),
	)
	setvar('fake_mac', mac)

def reset():
	command = ['ethtool', '-P', variables['interface']]
	output = subprocess.Popen( command, stdout=subprocess.PIPE ).communicate()[0]
	realmac = str(output)
	realmac = realmac.replace("b'Permanent address: ", "")
	realmac = realmac.replace("'", "")
	realmac =  realmac[:-2]
	if not realmac:
		print(colors.red+"[!] error"+colors.end)
	else:
		print(colors.blue+"realmac: "+realmac)
		xterm1a = "service network-manager stop"
		xterm2a = "ifconfig "+variables['interface']+" hw ether "+realmac
		xterm3a = "service network-manager start"
		print("[*] setting real mac"+colors.yellow)
		os.system(xterm1a)
		print(colors.green+"trying to set real mac address..."+colors.yellow)
		os.system(xterm2a)
		os.system(xterm3a)
		print(colors.green+"done!"+colors.end)