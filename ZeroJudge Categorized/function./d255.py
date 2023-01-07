import math

def A(a):
    g = 0
    for i in range(1, a):
        for j in range(i + 1, a + 1):
            g += math.gcd(i, j)
    return g

n = int(input())
while n != 0:
    print(A(n))
    n = int(input())