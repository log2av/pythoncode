import os
import paramiko 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.171.179.98', username="abhishek", password="xxxxx")
sftp = ssh.open_sftp()
localpath = 'abc.txt'
remotepath = '/opt/crestelsetup/patchzip/abc.txt'
sftp.put(localpath, remotepath)
sftp.close()
ssh.close()