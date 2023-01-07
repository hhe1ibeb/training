import math 

x = 1; n = int(input())
while n >= 0:
    if n & (n-1) == 0:
        y = math.log2(n)
    else:
        y = math.log2(n) + 1
    print("Case %d: %d" % (x, y))
    x += 1; n = int(input())