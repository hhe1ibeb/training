m, n, h = map(int, input().split())

land = []
for i in range(m):
    land.append([])
    for j in range(n):
        land[i].append(0)

for i in range(h):
    r, c, act = map(int, input().split())
    if act == 0:
        land[r][c] = 1
        a = c+1
        b = r+1
        aTrue = 1
        bTrue = 1

        while land[r][a] != 1:
            print(r, a)
            a += 1
            if a == n:
                aTrue = 0
                break
        if aTrue:
            for each in range(c, a):
                land[r][each] = 1

        while land[b][c] != 1:
            print(b, c)
            b += 1
            if b == m:
                bTrue = 0
                break
        if bTrue:
            for each in range(r, b):
                land[each][c] = 1

        print(land)

# not finished... this is tiring
