#1 1 2 3 5 8 13 21
a = 0
b = 1
for x in range(1, 100):
    c = a + b
    print c
    b = a
    a = c