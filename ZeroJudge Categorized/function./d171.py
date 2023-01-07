try:
    while True:
        n, m = [int(i) for i in input().split(' ')]
        x = n ** m
        print(len(str(x)))
except EOFError:
    pass