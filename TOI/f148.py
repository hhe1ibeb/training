w, h = map(int, input().split())
n = int(input())
land = []
alphabet_count = 0
for i in range(w):
    land.append(list(input().split()))
    alphabet_count += h - land[i].count('0')
if alphabet_count < n:
    print('Mission fail.')
else:
    asc = 97
    while n > 0:
        found = 0
        for i in range(w):
            for j in range(h):
                if land[i][j] == chr(asc):
                    found = 1
                    print(i, j)
        asc += 1
        if found:
            n -= 1
