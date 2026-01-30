from ipaddress import *

network = ip_network(f'191.128.66.83/255.192.0.0', 0)


print(network)
print(network.broadcast_address-1)
# for ip in network:
#     print(ip)

print(network[-2])