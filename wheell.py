import itertools, sys, time
spinner = itertools.cycle(['a', 'ab', 'abh', 'abhi', 'abh', 'ab'])
while True:
    sys.stdout.write(spinner.next())  # write the next character
    sys.stdout.flush()                # flush stdout buffer (actual character display)
    sys.stdout.write('\b') 
    time.sleep(1)