t = int(input())
for k in range(t):
    a = int(input()); b = int(input())
    x = 0
    for i in range(a, b+1):
        if i**0.5%1 == 0:
            x += i
    print('Case %d: %d' % (k+1, x))