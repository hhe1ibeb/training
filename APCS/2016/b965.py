try:
    while True:
        r, c, m = map(int, input().split())
        arrA = []
        arrB = []
        for i in range(r):
            arrB.append([int(i) for i in input().split()])
        action = list(map(int, input().split()))
        arrA = arrB
        for act in action[::-1]:
            r = len(arrA)
            c = len(arrA[0])
            arrC = []
            if act == 1:
                for i in range(r):
                    arrC.append(arrA[r-i-1])
            else:
                for i in range(c):
                    arrC.append([])
                    for j in range(r):
                        arrC[i].append(arrA[j][c-i-1])
            arrA = arrC
        r = len(arrA)
        c = len(arrA[0])
        print(r, c)
        for i in range(r):
            for j in range(c):
                if j != c-1:
                    print(arrA[i][j], end=' ')
                else:
                    print(arrA[i][j])
except EOFError:
    pass
