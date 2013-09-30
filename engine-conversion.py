import fileinput
import os
while True:
    table = raw_input('Enter the name of table ')
    cmd1='mysqldump -pabhishek --no-data -R --triggers cookie ' + table+ ' > '+table+'.sql'
    print(cmd1)
    fname= table+'.sql'
    print fname
    os.system(cmd1)
    for line in fileinput.FileInput(fname, inplace=1):
        line= line.replace('MyISAM', 'InnoDB')
        print line,
    cmd2='mysqldump -pabhishek --no-create-info -R --triggers cookie ' + table + ' > '+table+'_data.sql'
    print cmd2
    os.system(cmd2)
    cmd3='mysql -pabhishek cookie < '+table+'.sql'
    os.system(cmd3)
    print cmd3
    cmd4='mysql -pabhishek cookie < '+table+'_data.sql'
    print cmd4
    os.system(cmd4)
    print 'Conversion successful for ' + table