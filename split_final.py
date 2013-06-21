#!/root/python/Python-3.3.0/python

import os
import time
import datetime
date1 = time.strftime('%Y%m%d%H%M%S') 
f = open('/root/mypython/dblist.txt') # this files contains the name of databases
line = f.readline()
f.close()
words = line.split()
for word in words:
    cmd = "mysqldump -u root -pabhishek {0} > {0}_{1}.sql".format(word, date1) # takes backup in the same location as script
    cmd2 = "zip {0}_{1}.zip {0}_{1}.sql".format(word, date1) # zips the backup just taken
    cmd3 = "rm -f {0}_{1}.sql".format(word, date1) # deletes the .sql backup just taken. after this step only .zip backup remains. remove this line if u need both .sql and .zip
    cmd4 = " mv {0}_{1}.zip /backupdb ".format(word, date1)    
    cmd5 = " scp {0}_{1}.zip root@192.168.1.105:/home/laitkor/dev_test ".format(word, date1)
    os.system(cmd)
    os.system(cmd2)
    os.system(cmd3)
   # os.system(cmd4)
    if os.system(cmd5)== 0:
        result = "Backup Successful"
print(result)

