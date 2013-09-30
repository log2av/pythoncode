#import Queue
import threading
#import urllib2
import os
color='color C7'
os.system(color)

while True:
    print('Enter name of server...')
    print('1. VM 105') 
    print('2. VM 184')
    print('3. apps')
    print('5. ddb5')
    print('6. ddb6') 
    print('8. cloudegg-alpha')
    print('9. mmpro')
    print('10. corp')
    print('11. ssd4_amelearning')
    print('12. ddb2')
    print('        ')
    print('......................................................................')

    server = input ('')
    
    #print(server) 
    def logon():
        if server == '1':
            cmd1='p -ssh root@192.168.1.105 -pw xxxxxxx'
            os.system(cmd1)
            return 0
        elif server == '2':
            cmd1='p -ssh root@192.168.1.184 -pw xxxxxxx'
            os.system(cmd1)
        elif server == '3':
            cmd1='p -ssh root@192.168.1.184 -pw xxxxxxx'
            os.system(cmd1)
        elif server == '4':
            cmd1='p -ssh root@192.168.1.184 3333 -pw xxxxxxx'
            os.system(cmd1)
        elif server == '5':
            cmd1='p -ssh root@192.168.1.184 3333 -pw xxxxxxx'
            os.system(cmd1)
        elif server == '6':
            cmd1='p -ssh root@192.168.1.184 3333 -pw xxxxxxx'
            os.system(cmd1)
        elif server == '7':
            cmd1='p -ssh root@192.168.1.184 3333 -pw xxxxxxx'
            os.system(cmd1)
        elif server == '8':
            cmd1='p -ssh root@192.168.1.184 -pw xxxxxxx'
            os.system(cmd1)
        elif server == '9':
            cmd1='p -ssh root@192.168.1.184 2222 -pw xxxxxxx'
            os.system(cmd1)
        elif server == '10':
            cmd1='p -ssh root@192.168.1.184 -pw xxxxxxx'
            os.system(cmd1)
        elif server == '11':
            cmd1='p -ssh root@192.168.1.184 -pw xxxxxxx'
            os.system(cmd1)
        elif server == '12':
            cmd1='p -ssh root@192.168.1.184 3333 -pw xxxxxxx'
            os.system(cmd1)
    #logon()
    t = threading.Thread(target=logon())
    t.daemon = True
    t.start()