n, m, k = map(int, input().split())
count = k
kings = []
for i in range(k):
    kings.append(list(map(int, input().split())))

bomb_map = []
for i in range(n):
    bomb_map.append([0]*m)

for i in range(k):
    bomb_map[kings[i][0]][kings[i][1]] = 1

while count > 0:
    pop_list = []
    for i in range(len(kings)):
        s = kings[i]
        if s[0]+s[2] > m or s[1]+s[3] > n:
            pop_list.append(i)
            count -= 1
        elif bomb_map[s[0]+s[2]][s[1]+s[3]] == 1:
            pop_list.append(i)
            bomb_map[s[0]+s[2]][s[1]+s[3]] = 0
            count -= 1
        else:
            kings[i][0] += s[2]
            kings[i][1] += s[3]
            bomb_map[kings[i][0]][kings[i][1]] = 1
    for each in pop_list[::-1]:
        kings.pop(each)

bomb_count = 0
for i in range(n):
    for j in range(m):
        if bomb_map[i][j] == 1:
            bomb_count += 1
print(bomb_count)
