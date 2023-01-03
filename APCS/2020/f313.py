r, c, k, m = map(int, input().split())
land = [[-1]*(c+2)]
for i in range(1, r+1):
    land.append(list(map(int, input().split())))
    land[i].insert(0, -1)
    land[i].append(-1)
land.append([-1]*(c+2))
r += 2
c += 2

nums = []

for times in range(m):
    move_people = []
    for i in range(r):
        move_people.append([-1]*c)

    for i in range(1, r-1):
        for j in range(1, c-1):
            if land[i][j] == -1:
                pass
            move_people[i][j] = land[i][j]//k

    for i in range(1, r-1):
        for j in range(1, c-1):
            if move_people[i][j] >= 0:
                ppl = move_people[i][j]
                if move_people[i+1][j] >= 0:
                    land[i][j] -= ppl
                    land[i+1][j] += ppl
                if move_people[i-1][j] >= 0:
                    land[i][j] -= ppl
                    land[i-1][j] += ppl
                if move_people[i][j+1] >= 0:
                    land[i][j] -= ppl
                    land[i][j+1] += ppl
                if move_people[i][j-1] >= 0:
                    land[i][j] -= ppl
                    land[i][j-1] += ppl

for i in range(1, r-1):
    for j in range(1, c-1):
        if land[i][j] >= 0:
            nums.append(land[i][j])

print(min(nums))
print(max(nums))
