import random
a= random.randint(100000000, 900000000)
a = str(a)
c = ''
for x in range (1, 50):
    seq='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()+'
    b=random.choice(seq)
    c= c + b
d= a + c
password = list(d)
random.shuffle(password)
result = ''.join(password)

while True:
    num = int(input('Enter the length of password between 5 to 50 '))
    if num > 50 or num < 5:
        print('Inefficient or insufficient length provided')
    else:
        break

while True:
    if len(result) > num:
        result = result[1:]
    else:
        break
print(result)
input()
