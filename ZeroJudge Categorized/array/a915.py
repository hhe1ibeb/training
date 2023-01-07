n = int(input())
pos = []
for i in range(n):
    pos.append([int(j) for j in input().split(' ')])
pos.sort()
for i in range(n):
    for j in range(2):
        print(pos[i][j], end=' ')
    print()