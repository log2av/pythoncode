import mimetypes

# Import the email modules we'll need
import email
import email.mime.application
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib

# Create a text/plain message
msg = email.mime.Multipart.MIMEMultipart()
msg['Subject'] = 'Greetings'
msg['From'] = 'mysender@gmail.com'
msg['To'] = 'receiver@gmail.com'

# The main body is just another attachment
body = email.mime.Text.MIMEText("""Hello, how are you? I am fine.
This is a rather nice letter, don't you think?""")
msg.attach(body)

# PDF attachment
filename='cache/20140210204804.kml'
fp=open(filename,'rb')
att = email.mime.application.MIMEApplication(fp.read(),_subtype="kml")
fp.close()
att.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(att)

# send via Gmail server
# NOTE: my ISP, Centurylink, seems to be automatically rewriting
# port 25 packets to be port 587 and it is trashing port 587 packets.
# So, I use the default port 25, but I authenticate. 
s = smtplib.SMTP('smtp.gmail.com')
s.starttls()
s.login('mysender@gmail.com','password')
s.sendmail('mysender@gmail.com',['receiver@gmail.com'], msg.as_string())
s.quit()