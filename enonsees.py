ip="127.0.0.1"
lis_ip=ip.replace('.','')
total=0

for y in lis_ip:
    total+=int(y)

print(total* int(lis_ip[0]))