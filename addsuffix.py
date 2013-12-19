import subprocess
import fileinput
import sys

prefix = raw_input('Enter the prefix ')
suffix = raw_input('Enter the suffix ')
open('mytext.txt', 'w').close()
subprocess.call(['notepad.exe', 'mytext.txt'])
for line in fileinput.input('mytext.txt', inplace=True):
	line = line.rstrip()
	line = prefix + ' ' + line + ' ' + suffix + '\n'
	sys.stdout.write(line)
subprocess.call(['notepad.exe', 'mytext.txt'])
