import math
t = int(input())
for i in range(t):
    n, m = [int(i) for i in input().split()]
    n -= 2; m -= 2
    n = math.ceil(n / 3); m = math.ceil(m / 3)
    print(n * m)