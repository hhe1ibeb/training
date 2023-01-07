try:
    while True:
        inp = [int(i) for i in input().split(' ')]
        n = inp[0]; inp.remove(n)
        if sum(inp) / n > 59:
            print('no')
        else:
            print('yes')
except EOFError:
    pass