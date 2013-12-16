import subprocess
import fileinput
import sys
import os

date = raw_input('Enter the date in format YYYYMMDD ')
open('top10.txt', 'w').close()
subprocess.call(['notepad.exe', 'top10.txt'])
for line in fileinput.input('top10.txt', inplace=True):
	line = line.rstrip()
	line = 'zcat *' + date + '* | grep -a ' + line + ' > /opt/crestelsetup/report_temp/' + line + '.txt ; '
	#line = prefix + ' ' + line + ' ' + suffix + '\n'
	sys.stdout.write(line)
subprocess.call(['notepad.exe', 'top10.txt'])
os.remove('top10.txt')
