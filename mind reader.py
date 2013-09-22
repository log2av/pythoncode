import time
st1="""  
  __  __   _               _       _____                       _               
 |  \/  | (_)             | |     |  __ \                     | |              
 | \  / |  _   _ __     __| |     | |__) |   ___    __ _    __| |   ___   _ __ 
 | |\/| | | | | '_ \   / _` |     |  _  /   / _ \  / _` |  / _` |  / _ \ | '__|
 | |  | | | | | | | | | (_| |     | | \ \  |  __/ | (_| | | (_| | |  __/ | |   
 |_|  |_| |_| |_| |_|  \__,_|     |_|  \_\  \___|  \__,_|  \__,_|  \___| |_|  
 """
print(st1)
input('Pick a number between 2 and 9. Press enter to continue....')
input('Multiply this number by 9. Press enter to continue....')
input('If you have got 2 digits, add them. Press enter to continue....')
input('Subtract 5 from the added number. Press enter to continue....')
input('Pick a Alphabet according to your answer, A=1, B=2, C=3, D=4, E=5 and so on...')
#input('Press enter to continue....')
input('Name a Country with that Alphabet. Press enter to continue....')
input('With the second letter of that country, name a animal. Press enter to continue.')
input('Finally name the color of that animal. Press enter to continue....')
print('')
print('Mind Reader will now analyse your mind and try to predict your answers.')
print('Please wait few seconds while computer is doing calculations...............')
for x in range(1, 20):
    print('.' * x, end="\r")
    time.sleep(1)
#time.sleep(14)
print('')
print( 'and we are back.....')
time.sleep(2)
print('Lets see what we got')
time.sleep(4)
print('The country you thought is DENMARK')
time.sleep(4)
print('The animal you chose is ELEPHANT')
time.sleep(4)
print('The color you chose is BLACK or GRAY')
time.sleep(4)
input('Thanks for using this program. This software is created by Abhishek Verma. Press any key to exit...')