import re

m = '   0:	fe010113          	addi	sp,sp,-32'
p = r'^\s+(\w+):\s+(\w+)\s+(.+)'
l = re.match(p,m)

print(pa[0])

print(pa)