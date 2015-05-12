my_words = ['this: id']
a = set()
with open('got.txt') as f:
    for line in f:
	if any(word in line for word in my_words):
            a.add(line)
print len(a)