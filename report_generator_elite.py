import os
import sys
import paramiko
import fileinput
import datetime

#Login to DB1 and fetch the command output
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.171.17.00', username='root', password='xxxxxxxx')
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

#Login to db2 and fetch the command output
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.171.17.00', username='root', password='xxxxxxxxxx')
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
ssh.connect('10.171.17.00', username='c', password='xxxxxxx')
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

#Change last modified time of SAR file

os.utime('SAR.txt', None)

	
#Rename excel sheet
mylist = []
today = datetime.date.today()
mylist.append(today)
#print mylist[0]
date1 = str(mylist[0])

a =  os.listdir('.')
#print a
for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
  base_file, ext = os.path.splitext(filename)
  if ext == ".xlsx":
    os.rename(filename, 'Health_Chk_Report_LKO_' + date1 +'.xlsx')
	
#Delete older partition_log.txt file
os.remove('partition_log.txt')

#Run the batch file which creates partition log 
from subprocess import Popen
p = Popen("partition_report.bat", cwd=r"C:\Users\ankur\Desktop\Automated Report")
stdout, stderr = p.communicate()
	

    



