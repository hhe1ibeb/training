try:
    while True:
        n, m = [int(i) for i in input().split(' ')]
        if n == m:
            print(m)
        else:
            print(m + 1)
except EOFError:
    pass