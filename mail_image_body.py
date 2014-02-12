from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib

server = 'smtp.gmail.com'
port = 587
sender = 'abc@gmail.com'
recipient = 'abc@gmail.com'


# Create message and set message fields
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'
msgRoot['From'] = sender
msgRoot['To'] = recipient
msgRoot.preamble = 'This is a multi-part message in MIME format.'

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# Actual message body (with the image in the HTML code)
msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!', 'html')
msgAlternative.attach(msgText)

# Open image and read it
fp = open('cache/ava.PNG', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Attach image to 'image1' in the e-mail
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)


# Send message
session = smtplib.SMTP(server, port)
session.starttls()
session.login(sender, 'senderpassword')

session.sendmail(sender, recipient, msgRoot.as_string())
session.quit()