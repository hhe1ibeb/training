n, m = map(int, input().split())

land_map = []
for i in range(n):
    land_map.append(list(map(int, input().split())))

walked = []
for i in range(n):
    walked.append([0]*m)

min_value = min(land_map[0])
x = land_map[0].index(min_value)
y = 0
for i in range(1, n):
    for j in range(m):
        if land_map[i][j] < min_value:
            min_value = land_map[i][j]
            x = j
            y = i
walked[y][x] = 1

s = land_map[y][x]
while True:
    walkable = []
    if x+1 < m:
        if walked[y][x+1] == 0:
            walkable.append([land_map[y][x+1], x+1, y])
    if x-1 >= 0:
        if walked[y][x-1] == 0:
            walkable.append([land_map[y][x-1], x-1, y])
    if y+1 < n:
        if walked[y+1][x] == 0:
            walkable.append([land_map[y+1][x], x, y+1])
    if y-1 >= 0:
        if walked[y-1][x] == 0:
            walkable.append([land_map[y-1][x], x, y-1])
    if not len(walkable) > 0:
        break
    walkable.sort()
    x = walkable[0][1]
    y = walkable[0][2]
    s += land_map[y][x]
    walked[y][x] = 1

print(s)
