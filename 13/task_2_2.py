from ipaddress import *

ip_addr = ip_address('191.128.66.83')
ip_mask = ip_address('255.192.0.0')

network = ip_network(f'{ip_addr}/{ip_mask}', 0)

# for ip in network:
#     print(ip)

print(network)
print(network[-2])
print(network.broadcast_address - 1)