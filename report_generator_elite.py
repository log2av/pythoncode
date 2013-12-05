import os
import sys
import paramiko
import fileinput
import datetime

#Login to DB1 and fetch the command output
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.171.17.185', username='root', password='abcd')
stdin, stdout, stderr = ssh.exec_command("tail -100 /home/oracle/diag/rdbms/cgklck/CGKLCK1/trace/alert_CGKLCK1.log")
sys.stdout = open('alert_CGKLCK1.txt', 'w')
type(stdin)
print stdout.readlines()
sys.stdout.close()
for line in fileinput.input('alert_CGKLCK1.txt', inplace= True):
	line=line.replace('\\n', '\n')
	line=line.replace('[\'', '')
	line=line.replace('\']', '')
	line=line.replace('\', \'', '')
	sys.stdout.write(line)
ssh.close()

#Login to db2 and fetch the command output .. remove 1 for access
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.171.17.190', username='root', password='abcd')
stdin, stdout, stderr = ssh.exec_command("tail -100 /home/oracle/diag/rdbms/cgklck/CGKLCK2/trace/alert_CGKLCK2.log")
sys.stdout = open('alert_CGKLCK2.txt', 'w')
type(stdin)
print stdout.readlines()
sys.stdout.close()
for line in fileinput.input('alert_CGKLCK2.txt', inplace= True):
	line=line.replace('\\n', '\n')
	line=line.replace('[\'', '')
	line=line.replace('\']', '')
	line=line.replace('\', \'', '')
	sys.stdout.write(line)
ssh.close()

#Login to gtp1 and fetch the command output
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.171.17.183', username='crestel', password='abced')
stdin, stdout, stderr = ssh.exec_command("cat /opt/crestelsetup/crestelmediation/modules/mediation/bin/health.txt")
sys.stdout = open('GTP Summary.txt', 'w')
type(stdin)
print stdout.readlines()
sys.stdout.close()
for line in fileinput.input('GTP Summary.txt', inplace= True):
	line=line.replace('\\n', '\n')
	line=line.replace('[\'', '')
	line=line.replace('\']', '')
	line=line.replace('\', \'', '')
	line=line.replace('x1b', '')
	line=line.replace('[2J', '')
	line=line.replace('[1;1H', '')
	line=line.replace('\\\\\\r', '')
	sys.stdout.write(line)
ssh.close()

#make changes in SAR file
for line in fileinput.input('SAR.txt', inplace= True):
	line=line.replace('Linux', ' Linux')
	sys.stdout.write(line)
	line=line.replace(' Linux', 'Linux')
	sys.stdout.write(line)
	
#Rename excel sheet
mylist = []
today = datetime.date.today()
mylist.append(today)
print mylist[0]
date1 = str(mylist[0])

a =  os.listdir('.')
print a
for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
  base_file, ext = os.path.splitext(filename)
  if ext == ".xlsx":
    os.rename(filename, 'Health_Chk_Report_LKO_' + date1 +'.xlsx')
	

    



