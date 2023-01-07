try:
    while True:
        n, k = [int(i) for i in input().split(' ')]
        if k == 0:
            if n == 0:
                print('Ok!')
            else:
                print('Impossib1e!')
        else:
            if n % k == 0:
                print('Ok!')
            else:
                print('Impossib1e!')
except EOFError:
    pass