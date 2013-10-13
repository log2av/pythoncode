import os
import fileinput
import sys
#from fnmatch import fnmatch

root = '/root/mypython/log'
#pattern = "*.py"
names = []
for path, subdirs, files in os.walk(root):
    for name in files:
        filenames = os.path.join(path, name)
        print 'ok1111111'
        print filenames
        names.append(filenames)
print 'ok2222222222'
print names 
for item in names:
    print 'ok3333333333'
    print item
    for line in fileinput.input(item, inplace=True):
        line = line.replace('dude', 'verma')
        sys.stdout.write(line)
        #print 'string replaced in' + item
