def isPrime(a):
    if a == 1: return 0
    if a == 2: return 1
    for i in range(2, a//2+1):
        if a % i == 0:
            return 0
    return 1

try:
    while True:
        a, b = [int(i) for i in input().split(' ')]
        count = 0
        for i in range(a, b+1):
            count += isPrime(i)
        print(count)
except EOFError:
    pass