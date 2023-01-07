def isPrime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

try:
    while True:
        inp = input()
        x = 0
        for i in inp:
            k = 0
            if i.isupper():
                k = ord(i) - 38
            else:
                k = ord(i) - 96
            x += k
        if isPrime(x):
            print('It is a prime word.')
        else:
            print('It is not a prime word.')
except EOFError:
    pass