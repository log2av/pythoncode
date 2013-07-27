import webbrowser
import string
import subprocess
import fileinput
import sys
import re

doda='/autodeals/filldatabase'


open('sites.txt', 'w').close()
subprocess.call(['notepad.exe', 'sites.txt'])
for line in fileinput.input('sites.txt', inplace=True):
    line = line.replace("\n", " ")
    sys.stdout.write(line)



f = open('sites.txt')
text1 = f.read()
f.close()

print(text1) 

websites = re.findall(r'(\S+[.]com)', text1)
print(websites)
data = ', '.join(websites)
print(data)
data1 = data.replace(",", "")
print(data1)

words = data1.split()
for word in words:
    url = 'http://' + word + doda
    print(url)
    webbrowser.open(url)
s = input('Press any key to continue...')


