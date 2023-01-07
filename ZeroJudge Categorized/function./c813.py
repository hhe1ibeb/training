def f(n):
    if n >= 10:
        return f(sum([int(i) for i in str(n)]))
    return n

n = int(input())
while n != 0:
    print(f(n))
    n = int(input())