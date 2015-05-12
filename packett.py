with open('log.txt', 'r') as f:
    drops = {}
    for line in f:
         if 'drops' in line:
             time, ip, fn, n, packets = line.split()
             print ip
             drops[ip] = drops.get(ip, 0) + int(n)
             print drops
for ip, count in drops.items():
    print ip, count