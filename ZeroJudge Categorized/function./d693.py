import math

def lcm(a, b):
    return abs(a * b) / math.gcd(a, b)

try:
    while True:
        n = int(input()); x = 0
        inp = [int(j) for j in input().split(' ')]
        for i in range(1, n):
            if i != 1:
                x = int(lcm(inp[i], x))
            else:
                x = int(lcm(inp[i], inp[i-1]))
        print(int(x))
except EOFError:
    pass