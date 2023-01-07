def fib(n):
    return recursive(n)[1]

def recursive(n):
    # calculate f(n+1) and f(n)
    if n == 0:
        return 1, 0
    
    q, r = divmod(n, 2)
    f2, f1 = recursive(q) # f2 is the larger one
    f2, f1 = f1 ** 2 + f2 ** 2, f1 * (2 * f2 - f1)
    if r == 0:
        return f2, f1
    return f1 + f2, f2
    
try:
    while True:
        n = int(input())
        print(fib(n+1))
except EOFError:
    pass