shape = {"A": [4, 1], "B": [1, 3], "C": [2, 2]}
r, c, n = map(int, input().split())
store = []
pkg = []
unpushed = 0
for i in range(r):
    store.append([0]*c)
for i in range(n):
    # x = input().split()
    # pkg.append([x[0], int(x[1])])
    tp, y = input().split()
    y = int(y)
    cur = []
    if tp != "D" and tp != "E":
        a, b = shape[tp]
        for j in range(a):
            cur.append([])
            for k in range(b):
                cur[j].append(1)
    if tp == "D":
        cur.append([0, 0, 1])
        cur.append([1, 1, 1])
    if tp == "E":
        cur.append([0, 1])
        cur.append([1, 1])
        cur.append([1, 1])
    able = 0
    x = 0
    for j in range(len(cur)):
        if store[j+y].count(0) > cur[j].count(1):
            able = 1
        else:
            unpushed += 1
        for k in range(c-1, 0, -1):
            if store[j+y][k] == 1:
                if k > x:
                    x = k + 1
    if (able):
        for j in range(len(cur)):
            for k in range(len(cur[0])):
                store[y+j][x+k] = cur[j][k]
    else:
        unpushed += 1
    print(store)
blank = 0
for i in range(r):
    blank += store[i].count(0)
print(blank, unpushed)
