import os
from collections import Counter
f = open('log.txt')
line = f.readlines()
print line
f.close()
a = Counter(line)
print a
no_exist = line.count(======== MOBILITY EVENT (G): ATTACH REJECT =========\n)
print 'The records are: ' + no_exist
#for index, word in enumerate(line):
	#print index, word
#words = line.split()
#print words