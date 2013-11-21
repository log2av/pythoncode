import os
import fileinput
imsi1=[]
f = open(u'log.txt', u'r')
f.close()
line1=[]
#line1 = f.extend(eachLine.split())

for line in fileinput.input('log.txt', inplace=True):
	line1 = line.split(':')
	print line1
	print line
	#if line[0] == 'IMSI':
		#imsi1.append(line[1])
        #line = prefix + ' ' + line + ' ' + suffix + '\n'
        #sys.stdout.write(line)

print imsi1
print line1
raw_input()