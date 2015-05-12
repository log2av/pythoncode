import subprocess
import fileinput
import sys
#change default separator here
sepe = raw_input('Enter the seperator ') or '|'
open('mytext.txt', 'w').close()
subprocess.call(['notepad.exe', 'mytext.txt'])
for line in fileinput.input('mytext.txt', inplace=True):
    tmpline = line.split(sepe)
    line = tmpline[0] + '\n'
    sys.stdout.write(line)
subprocess.call(['notepad.exe', 'mytext.txt'])
