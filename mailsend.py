import smtplib
 
#SMTP_SERVER = 'smtp.gmail.com'
#SMTP_PORT = 587
server = 'smtp.gmail.com'
port = 587

sender = 'log2av@gmail.com'
recipient = 'log2av@live.com'
subject = 'Gmail SMTP Test'
body = 'blah blah blah'
 
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
session.login(sender, 'password_mail')
 
session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
session.quit()
