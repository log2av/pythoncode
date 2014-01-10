import itertools
from itertools import izip
good_words = ['IMSI', 'RA New']

with open('log.txt') as oldfile, open('lognew.txt', 'w') as newfile:
    for line in oldfile:
        if any(word in line for word in good_words):
            newfile.write(line)
with open('num.txt', 'r') as f:
    for line1, line2, line3 in izip(f, f, f):
        print line1.rstrip('\n') + ' ' + line2.rstrip('\n') + ' ' + line3
			
			
#with open('lognew.txt', 'r') as f:
#	firstlines = itertools.islice(f, 0, None, 1)
#	secondlines = itertools.islice(f, 0, None, 2)
#	for line1 in firstlines :
#		print line1
#	for line2 in secondlines :
#		print line2
#	for (line1 in firstlines) and (line2 in secondlines):
#		print line1 + line2 