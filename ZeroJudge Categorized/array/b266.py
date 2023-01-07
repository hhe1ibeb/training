try:
    while True:
        r, c, m = [int(i) for i in input().split(' ')]
        arrB = []
        for i in range(r):
            arrB.append([int(k) for k in input().split(' ')])
        oper = [int(i) for i in input().split(' ')]
        oper = oper[::-1]
        arrA = []
        t = 0
        for i in range(m):
            act = oper[i]
            if act == 1:
                for j in range(r):
                    arrA.append(arrB[r-j-1])
            else:
                t += 1
                if t % 2 == 0:
                    for j in range(r):
                        arrA.append([])
                        for k in range(c):
                            arrA[j].append(arrB[r-j-2][c-k-1])
                else:
                    for j in range(c):
                        arrA.append([])
                        for k in range(r):
                            arrA[j].append(arrB[r-j-2][c-k-1])
        print(arrA)
except EOFError:
    pass