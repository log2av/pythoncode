import subprocess
import fileinput
import sys





open('file.txt', 'w').close()
subprocess.call(['notepad.exe', 'file.txt'])
for line in fileinput.input('file.txt', inplace=True):
    line = line.replace("\\","/")
    line = line.replace("\n"," ")
    #line = line.replace("  ", " ")
    line = line.replace("\\\\192.168.1.184\\laitcoin\\", "")
    line = line.replace("Z:/SMT_14_apr/", "")
    line = line.replace("\\\\192.168.1.184\\laitcoin\\", "")
    line = line.replace("Sending","")
    line = line.replace("Transmitting file data ..........","")
    line = line.replace("Adding", "")
    line = line.replace("(bin)","")
    line = line.replace("//192.168.1.184/hiplinkportal/","")
    line = line.replace("/sites/hiplinkportal/", "")
    line = ''.join(line.split())
    line = line + " "


    sys.stdout.write(line)
subprocess.call(['notepad.exe', 'file.txt'])