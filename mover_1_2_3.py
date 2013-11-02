import os
import os.path
import fileinput
import sys
import shutil
#from fnmatch import fnmatch

#root = '/root/mypython/log'

src1 = 'D:\\doc'
des1 = 'E:\\vbox'


def check_file(self, n):
	
	name = '.'.join(self.split('.')[:-1])
	ext = self.split('.')[-1]
	
	if n==1:
		temp=self
	else:
		temp=name +'_'+ str(n) + '.' + ext
		
	if os.path.isfile(temp) == True:
		n= n + 1
		temp = check_file(self,n)
		
	return temp

full_path = []
full_dir = []
for path, subdirs, files in os.walk(src1):
	for name in files:
		filenames = os.path.join(path, name)
		full_path.append(filenames)

for item in full_path:
	f1 = item.split('\\')[-1]
	des4 = des1 + '\\' + f1
	des5 = check_file(des4,1)
	print(item + ' will be copied to ' + des5 )
	shutil.copyfile(item, des5)
    

		
		

