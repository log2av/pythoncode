import fileinput, sys, os, subprocess
import binascii
import socket
open('hexfile.txt', 'w').close()
subprocess.call(['notepad.exe', 'hexfile.txt'])
for line in fileinput.input('hexfile.txt', inplace = True):
	line = binascii.hexlify(socket.inet_aton(line)).upper()
	line = line + '\n'
	sys.stdout.write(line)
subprocess.call(['notepad.exe', 'hexfile.txt'])
os.remove('hexfile.txt')	

