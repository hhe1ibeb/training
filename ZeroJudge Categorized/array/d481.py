try:
    while True:
        a, b, c, d = [int(i) for i in input().split(' ')]
        multiplyable = (b==c)
        if multiplyable:
            arrA = []; arrB = []
            for i in range(a):
                arrA.append([int(k) for k in input().split(' ')])
            for i in range(c):
                arrB.append([int(i) for i in input().split(' ')])
            arrC = []
            for i in range(a):
                arrC.append([])
                for j in range(d):
                    x = 0
                    for k in range(b):
                        x += arrA[i][k] * arrB[k][j]
                    arrC[i].append(x)
            for i in range(a):
                for j in range(d):
                    print(arrC[i][j], end=' ')
                    if j == d - 1:
                        print()
        else:
            print('Error')
except EOFError:
    pass