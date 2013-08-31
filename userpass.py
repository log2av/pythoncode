#!/root/python/Python-3.3.0/python 
import string
import os
import random
import string
import smtplib

#user1=input('Enter the name of the user ')
user1='darklord'
pass1= ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(10))
cmd='echo -e "' + pass1 + '\n' + pass1 + '" | passwd ' + user1
if os.system(cmd)!= 0:
    print('Invalid User')
else:
    print('New password for user ' + user1 + ' is ' + pass1 )

#SMTP_SERVER = 'smtp.gmail.com'
#SMTP_PORT = 587
server = 'smtp.gmail.com'
port = 587

sender = 'myemail@gmail.com'
recipient = 'hisemail@laitkor.com'
subject = 'Change of Password'
body = 'New Password for user ' + user1 + ' is ' + pass1 
 
"Sends an e-mail to the specified recipient."
 
body = "" + body + ""
 
headers = ["From: " + sender,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)
 
session = smtplib.SMTP(server, port)
 
session.ehlo()
session.starttls()
session.ehlo
session.login(sender, 'yourpassword')
 
session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
session.quit()
