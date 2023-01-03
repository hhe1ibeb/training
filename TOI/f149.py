r, c = map(int, input().split())
land = []
bomb_count = 0
land.append([0]*(c+2))
for i in range(1, r):
    land.append(list(map(int, input().split())))
    land[i].insert(0, 0)
    land[i].append(0)
    bomb_count += land[i].count(1)
land.append([0]*(c+2))
print(land)
