try:
    while True:
        n, m = map(int, input().split(' '))
        full = []
        for i in range(n):
            full.append([int(k) for k in input().split(' ')])
        for i in range(m):
            x1, y1, x2, y2 = map(int, input().split(' '))
            sum = 0
            for j in range(y2-y1+1):
                for k in range(x2-x1+1):
                    sum += full[k][j]
            print(sum)
except EOFError:
    pass