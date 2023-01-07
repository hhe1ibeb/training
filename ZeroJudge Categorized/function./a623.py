import math

try:
    while True:
        n, m = [int(i) for i in input().split(' ')]
        print(int((math.factorial(n) / (math.factorial(m) * math.factorial(n - m)))))
except EOFError:
    pass