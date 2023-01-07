def f91(a):
    if a <= 100:
        return f91(f91(a + 11))
    else:
        return a - 10
try:
    while True:
        n = int(input())
        while n != 0:
            print("f91(%d) = %d" % (n, f91(n)))
            n = int(input())
except EOFError:
    pass