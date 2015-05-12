date1 = raw_input("Enter starting date ")
empty1 = raw_input('Enter first empty partition ')
empty2 = raw_input('Enter second empty partition ')
for x in range(int(date1), int(date1) + 10):
    #print x, x + 1
    print 'sh create_partitions.sh ' + str(x).zfill(2) + ' ' + str(x + 1 ).zfill(2) + ' ORADATA' + str(empty1)
for y in range(int(date1)+10, int(date1) + 20):
    #print x, x + 1
    print 'sh create_partitions.sh ' + str(y).zfill(2) + ' ' + str(y + 1 ).zfill(2) + ' ORADATA' + str(empty2)
