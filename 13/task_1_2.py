# 123.0.255.1
# 111110001111110000000101010101 -> 32
# 111111111111111111111100000000 -> 32

from ipaddress import *

# network = ip_network(f'192.168.32.160/255.255.255.240')
ip_net = ip_address('192.168.32.160')
ip_mask = ip_address('255.255.255.240')
network = ip_network(f'{ip_net}/{ip_mask}')

cnt = 0
for ip in network:
    bin_ip = f'{ip:b}'
    print(ip, bin_ip)
    if bin_ip.count('1') % 2 == 0:
        cnt += 1

print(cnt)

print(f'{ip_mask:b}')

# print(network)
# print(f'{ip_net:b}')
# print(network[1])
