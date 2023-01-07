try:
    while True:
        b, n = [int(i) for i in input().split(' ')]; d = len(str(n))
        a = [int(i) for i in str(n)]; x = 0
        for i in a:
            x += i ** d
        if n == x:
            print('YES')
        else:
            print('NO')
except EOFError:
    pass