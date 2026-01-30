from ipaddress import *

ip_net = ip_address('192.168.32.160')
ip_mask = ip_address('255.255.255.240')

network = ip_network(f'{ip_net}/{ip_mask}')

print(bin(int(ip_net)))
print(bin(int(ip_mask)))

print(network)

print('*'*70)
cnt = 0
for ip in network:
    ip_bin = bin(int(ip))
    print(ip, '->', ip_bin, ip_bin.count('1'))
    if ip_bin.count('1') % 2 == 0:
        cnt += 1
print(cnt)

