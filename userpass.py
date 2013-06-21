import string
import os
import random
import string
user1=input('Enter the name of the user ')
pass1= ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(10))
cmd='echo -e "' + pass1 + '\n' + pass1 + '" | passwd ' + user1
if os.system(cmd)!= 0:
    print('Invalid User')
else:
    print('New password for user ' + user1 + ' is ' + pass1 )



