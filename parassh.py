import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1', username='jesse', password='lol')
ssh.connect('127.0.0.1', username='jesse', password='lol')
stdin, stdout, stderr = ssh.exec_command("uptime")
type(stdin)
stdout.readlines()
