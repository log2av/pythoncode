import os
from io import open
project = raw_input(u'Enter the name of project ')
domain = raw_input (u'Enter the domain ')
docroot = raw_input(u'Enter root folder ')
virtualhost=u"""
<VirtualHost *:80>
    ServerAdmin abhishek.verma@laitkor.com
    DocumentRoot /""" +docroot+ u"""/""" +project+ u"""
    ServerName """ +project+ u""".""" +domain+ u""".com
    ErrorLog logs/""" +project+ u""".com-error_log
    CustomLog logs/""" +project+ u""".com-access_log common
</VirtualHost>"""
f = open(u'/etc/httpd/conf/httpd.conf', u'a')
f.write(virtualhost)
f.close()

cmd1 = u'mkdir /' + docroot + u'/' + project
os.system(cmd1)

cmd2 = u'mysql -u root -pabhishek -e "create database ' +project+ u' "'
os.system(cmd2)

cmd3 = u'service httpd restart'
os.system(cmd3)

cmd4 = u'chmod -R 755 /' + docroot + u'/' + project
os.system(cmd4)

cmd4 = u'chown -R apache.apache /' + docroot + u'/' + project
os.system(cmd4)

print domain+ u' URL is ' +project+ u'.' +domain+ u'.com'
print u'DocumentRoot is /' +docroot+ u'/' +project
print u'Database Name is ' +project

