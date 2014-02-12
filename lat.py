import os
import glob
import os.path
import fileinput
import sys
import shutil

#directory='/path/to/dir'
#os.chdir(directory)
filelist=glob.glob("D:\\test\\*")
for f in filelist:
    os.remove(f)
newest = max(glob.iglob('*.[Pp][Nn][Gg]'), key=os.path.getctime)
print newest
source1 = 'C:\\Users\\ankur\\Desktop\\cache\\' + newest
des1 = 'D:\\test'
print source1
print des1
shutil.copy(source1, des1)