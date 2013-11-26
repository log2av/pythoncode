import os
import sys
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.124.128', username='root', password='keerti')
stdin, stdout, stderr = ssh.exec_command("tail -20 /home/alert.log")
sys.stdout = open('alert.txt', 'w')
type(stdin)
print stdout.readlines()
sys.stdout.close()
for line in fileinput.input('alert.txt', inplace= True):
	line=line.replace('\\n', '\n')
	line=line.replace('[\'', '')
	line=line.replace('\']', '')
	line=line.replace('\', \'', '')
	sys.stdout.write(line)
ssh.close()
