import Image, os
import os
path = "C:\\Users\\Ajju\\Desktop\\test_images"
for filename in os.listdir(path):
    img = Image.open(path + '\\' + filename)
    clrs = img.getcolors()
    print filename, len(clrs)
    if len(clrs) == 1:
	    os.remove(path + '\\' + filename)
        #print filename + " Deleted"
		#print clrs
#clrs contains [("num of occurences","color"),...]

#By checking for len(clrs) == 1 you can verify if the image contains only one color and by looking at the second element of the first tuple in clrs you can infer the color.