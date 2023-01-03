n = int(input())
pos = []
dis = []
for i in range(n):
    pos.append(list(map(int, input().split())))
    if i > 0:
        dis.append(abs(pos[i][0]-pos[i-1][0])+abs(pos[i][1]-pos[i-1][1]))
print(max(dis), min(dis))
