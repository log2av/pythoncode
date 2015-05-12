import subprocess
import fileinput
import sys
from random import randint
counts = []

open('mytext.txt', 'w').close()
subprocess.call(['notepad.exe', 'mytext.txt'])
for line in fileinput.input('mytext.txt', inplace=True):
    text1 = line.split(':')
    #print text1[1]
    counts.append(text1[1])	
l = len(counts)
l = l / 3
i = 0
for x in range(1,l):
    #print i, i+1, i+2
    print int(counts[i]) + int(counts[i+1]) + int(counts[i+2])	
    i = i + 3