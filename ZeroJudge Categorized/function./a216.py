def f(i):
    return (i**2+i)//2
def g(i):
    return sum([f(i) for i in range(1, i+1)])

try:
    while True:
        n = int(input())
        print("%d %d" % (f(n), g(n)))
except EOFError:
    pass