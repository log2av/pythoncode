import subprocess
import fileinput
import sys
import os
open('file.txt', 'w').close()
subprocess.call(['notepad.exe', 'file.txt'])
for line in fileinput.input('file.txt', inplace=True):
    line = line.replace("/dev/sda3              ", "")
    line = line.replace("/dev/sda6              ", "")
    line = line.replace("/dev/sda2              ", "")
    line = line.replace("/dev/sda1              ", "")
    line = line.replace("tmpfs                  ", "")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b90000", "")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b90001","")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b90002","")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b90003", "")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b90004","")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b90005","")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b90006", "")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b90007", "")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b90008", "")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b90009", "")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b9000a", "")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b9000b", "")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b9000c", "")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b9000d","")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b9000e","")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b90024", "")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b90025","")
    line = line.replace("/dev/mapper/360060e8010209b900009001009b90026","")
    line = line.replace("                      ", "")
    line = line.replace("\n", " ")
    #line = ' '.join(line.split())
    line = line.replace("/u02 ", "\n")
    line = line.replace("/ ", "\n")
    line = line.replace("/u01 ", "\n")
    line = line.replace("/boot ", "\n")
    line = line.replace("/dev/shm ", "\n")
    line = line.replace("/ORADATA1 ", "\n")
    line = line.replace("/ORADATA2 ", "\n")
    line = line.replace("/ORADATA3 ", "\n")
    line = line.replace("/ORADATA4 ", "\n")
    line = line.replace("/ORADATA5 ", "\n")
    line = line.replace("/ORADATA6 ", "\n")
    line = line.replace("/ORASYS ", "\n")
    line = line.replace("/ORAREDO1 ", "\n")
    line = line.replace("/ORAREDO2 ", "\n")
    line = line.replace("/ORAREDO3 ", "\n")
    line = line.replace("/ORADATA7 ", "\n")
    line = line.replace("/ORADATA8 ", "\n")
    line = line.replace("/ORADATA9 ", "\n")
    line = line.replace("/ORADATA10 ", "\n")
    line = line.replace("/ORADATA11 ", "\n")
    line = line.replace("/ORADATA12 ", "\n")
    line = line.replace("/ORADATA13", "\n")
    line = line.replace("/ORATEMP ", "\n")
    line = line.lstrip()
    #line = line.replace(" 2.0T", "x2.0T")
    #line = line.replace(" 1.0T", "1.0T")
    #line = line.replace(" 5.0T", "5.0T")
    
	

	
	
	
    #line = ''.join(line.split())
    #line = line + " "
    sys.stdout.write(line)
subprocess.call(['notepad.exe', 'file.txt'])
os.remove('file.txt')