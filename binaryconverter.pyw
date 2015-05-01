import fileinput, sys, os, subprocess
import binascii
import socket, struct
open('hexfile2.txt', 'w').close()
subprocess.call(['notepad.exe', 'hexfile2.txt'])
for line in fileinput.input('hexfile2.txt', inplace = True):
    addr_long = int(line,16)
    line = socket.inet_ntoa(struct.pack("<L", addr_long))
	#line = binascii.hexlify(socket.inet_aton(line)).upper()
    #line = line + '\n'
    line1 = line.split('.')
    line2 = line1[3] + '.' + line1[2] + '.' + line1[1] + '.'+ line1[0]
    line2 = line2 + '\n'
    sys.stdout.write(line2)
subprocess.call(['notepad.exe', 'hexfile2.txt'])
os.remove('hexfile2.txt')	

