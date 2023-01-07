t = int(input())
for i in range(t):
    n, m = [int(i) for i in input().split(' ')]; arr = []
    k = n ** 2
    x, y = 0, 0
    x1, y1 = 0, 0; x2, y2 = n - 1, n -1
    for j in range(n):
        arr.append([0 for i in range(n)])
    direction = 1
    for j in range(1, k+1):
        if m == 1:
            arr[y][x] = j
        else:
            arr[x][y] = j

        if direction == 1: x += 1
        if direction == 2: y += 1
        if direction == 3: x -= 1
        if direction == 4: y -= 1
        
        if x == x2 and y == y1 and direction == 1:
            direction = 2
            y1 += 1
        if x == x2 and y == y2 and direction == 2:
            direction = 3
            x2 -= 1
        if x == x1 and y == y2 and direction == 3:
            direction = 4
            y2 -= 1
        if x == x1 and y == y1 and direction == 4:
            direction = 1
            x1 += 1
    for j in arr:
        for k in j:
            print('%5d' % k, end='')
        print()