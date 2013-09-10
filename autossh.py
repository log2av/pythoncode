import os
color='color C7'
os.system(color)

print('Enter name of server...')
print('1. VM 105') 
print('2. VM 184')
print('3. apps')
print('4. ddb2')
print('5. ddb5')
print('6. ddb6') 
print('7. vse')
print('8. cloudegg-alpha')
print('9. mmpro')
print('10. corp')
print('        ')

print('......................................................................')

server = input ('')
print(server) 
if server == '1':
    cmd1='p -ssh root@192.168.1.105 -pw m2n1shlko'
    os.system(cmd1)
if server == '2':
    cmd1='p -ssh root@192.168.1.184 -pw m2n1shlko'
    os.system(cmd1)
if server == '3':
    cmd1='p -ssh root@65.49.34.162 -pw L1fEexPresS@231'
    os.system(cmd1)
if server == '4':
    cmd1='p -ssh root@72.52.98.170 3333 -pw @ndr01d@ppend@231'
    os.system(cmd1)
if server == '5':
    cmd1='p -ssh root@65.49.52.180 3333 -pw g0lDen+emple@231'
    os.system(cmd1)
if server == '6':
    cmd1='p -ssh root@65.49.52.187 3333 -pw g0lDen+emple@231'
    os.system(cmd1)
if server == '7':
    cmd1='p -ssh root@72.52.98.162 3333 -pw @ndr01d@ppend@231'
    os.system(cmd1)
if server == '8':
    cmd1='p -ssh root@72.52.98.168 -pw @ndr01d@ppend@231'
    os.system(cmd1)
if server == '9':
    cmd1='p -ssh root@72.52.98.19 2222 -pw L1fEexPresS@231'
    os.system(cmd1)
if server == '10':
    cmd1='p -ssh root@65.49.34.175 -pw L1fEexPresS@231'
    os.system(cmd1)




