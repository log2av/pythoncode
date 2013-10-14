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
        names.append(filenames)
for item in names:
    for line in fileinput.input(item, inplace=True):
        line = line.replace('linux', 'android')
        sys.stdout.write(line)
    print 'String replaced in ' + item
