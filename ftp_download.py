import os
import paramiko 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.17.176.93', username="abhishek", password="xxxxxxxx")
sftp = ssh.open_sftp()
lp = os.path.realpath(__file__)
localpath = 'install-mediation-db.sh'
remotepath = '/opt/crestelsetup/patchzip/install-mediation-db.sh'
print localpath
print remotepath
sftp.get(remotepath, localpath)
sftp.close()
ssh.close()