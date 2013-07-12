import os
#import MySQLdb
project = input('Enter the name of project ')
domain = input ('Enter the domain ')
docroot = input('Enter root folder ')
virtualhost="""
<VirtualHost *:80>
    ServerAdmin abhishek.verma@laitkor.com
    DocumentRoot /""" +docroot+ """/""" +project+ """
    ServerName """ +project+ """.""" +domain+ """.com
    ErrorLog logs/""" +project+ """.com-error_log
    CustomLog logs/""" +project+ """.com-access_log common
</VirtualHost>"""
f = open('/etc/httpd/conf/httpd.conf', 'a')
f.write(virtualhost)
f.close()

cmd1 = 'mkdir /' + docroot + '/' + project
os.system(cmd1)

cmd2 = 'mysql -u root -pabhishek -e "create database ' +project+ ' "'
os.system(cmd2)

cmd3 = 'service httpd restart'
os.system(cmd3)

cmd4 = 'chmod -R 755 /' + docroot + '/' + project
os.system(cmd4)

cmd4 = 'chown -R apache.apache /' + docroot + '/' + project
os.system(cmd4)

print( domain+ ' URL is ' +project+ '.' +domain+ '.com')
print( 'DocumentRoot is /' +docroot+ '/' +project)
print( 'Database Name is ' +project)

