import os

domain = input('Enter the name of domain ')
vm = input('Enter the name of VM   1.105  2.184  3.103 ') 

if vm == '1':
    ip='192.168.1.105'
if vm == '2':
    ip='192.168.1.184'
if vm == '3':
    ip='192.168.1.103'

entry = '\n' + ip + ' ' + domain

f = open('C:\Windows\System32\Drivers\etc\hosts', 'a')
f.write(entry)
f.close()
print('Host entry Succeeded')




