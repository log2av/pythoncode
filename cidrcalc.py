from netaddr import IPNetwork
ipc = raw_input('Enter The IP Range ')
n = 0
#for ip in IPNetwork(ipc):
for ip in list(IPNetwork(ipc))[1:-1]:
    n = n + 1
    print '%s' % ip
print 'Total No of IPs are ' + str(n)
raw_input()