with open('hp.txt','r+') as f:
    old = f.read()
    f.seek(2)
    f.write('Lordooooo\n' + old)
f.close()