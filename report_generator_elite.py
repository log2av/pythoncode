import os
import sys
import paramiko
import fileinput

#Login to DB1 and fetch the command output
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.171.17.85', username='root', password='elite2013core')
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
ssh.connect('10.171.17.90', username='root', password='elite2013core')
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
ssh.connect('10.171.17.83', username='crestel', password='cr@st@l!0')
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



