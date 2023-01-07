try:
    while True:
        n = int(input())
        xpos = []; ypos = []
        k = 1
        for i in range(n):
            x, y = [int(i) for i in input().split(' ')]
            xpos.append(x)
            ypos.append(y)
            if i > 0 and i < n - 1:
                if xpos[i] > xpos[i - 1] and ypos[i] > ypos[i - 1]:
                    k += 1
        print(k)
except EOFError:
    pass