#os.system("taskkill /im chrome.exe /F")
import os
proc = os.popen("wmic process get description").read()
proclist = []
proc = proc.split()
proclist = proc
y = len(proclist)
print(y)
for x in range(1, y):
    print(proclist[x])
	s=input()

