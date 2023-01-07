def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True
x = 17
for i in range(11, 2000000):
    if isPrime(i):
        x += i
print(x)