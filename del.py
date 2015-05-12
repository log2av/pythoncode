my_words = ['16/04/2014']

with open('inputfile.txt') as oldfile, open('outputfile.txt', 'w') as newfile:
    for line in oldfile:
        if any(word in line for word in my_words):
            newfile.write(line)