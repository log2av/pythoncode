import subprocess
import fileinput
import sys
from random import randint

open('mytext.txt', 'w').close()
subprocess.call(['notepad.exe', 'mytext.txt'])
for line in fileinput.input('mytext.txt', inplace=True):
    # get all numbers from row
    numbers = [int(x) for x in line.strip().split()]
    if numbers[0] < 999:
        numbers = [x + randint(25,101) for x in numbers]
    else:
        numbers = [x + randint(50,500) for x in numbers]
    # re-map modified numbers to a line of text
    sys.stdout.write(' '.join([str(x) for x in numbers]) + '\n')
subprocess.call(['notepad.exe', 'mytext.txt'])