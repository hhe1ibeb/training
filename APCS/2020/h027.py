s, t, n, m, r = map(int, input().split())
arr_a = []
arr_b = []
for i in range(s):
    arr_a.append(list(map(int, input().split())))
for j in range(n):
    arr_b.append(list(map(int, input().split())))

sum_a = 0
for i in range(s):
    for j in range(t):
        sum_a += arr_a[i][j]

avaiable = []

for i in range(n-s+1):
    for j in range(m-t+1):
        different = 0
        for k in range(s):
            for l in range(t):
                if arr_b[i+k][j:j+t][l] != arr_a[k][l]:
                    different += 1
        if different <= r:
            avaiable.append([i, j])

arrs = []

for i in range(len(avaiable)):
    a, b = avaiable[i][0], avaiable[i][1]
    arrs.append([])
    for j in range(s):
        arrs[i].append(arr_b[a+j][b:b+t])

min_dis = 0

for times in range(len(arrs)):
    temp_sum = 0
    for i in range(s):
        for j in range(t):
            temp_sum += arrs[times][i][j]
    dis = abs(sum_a - temp_sum)
    if times == 0:
        min_dis = dis
    else:
        if dis < min_dis:
            min_dis = dis

if len(avaiable) == 0:
    print(0)
    print(-1)
else:
    print(len(avaiable))
    print(min_dis)
