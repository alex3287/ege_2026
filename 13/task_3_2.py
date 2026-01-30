from ipaddress import *

network = ip_network(f'172.16.168.0/255.255.248.0')

print(network)

cnt = 0
for ip in network:
    # bin_ip = bin(int(ip))[2:]
    bin_ip = f'{ip:b}'
    # print(ip, bin_ip, len(bin_ip))
    if bin_ip.count('1') % 5 != 0:
        cnt += 1
print(cnt)