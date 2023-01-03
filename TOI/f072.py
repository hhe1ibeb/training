n = int(input())
land = list(map(int, input().split()))
count = 0
start = 0
end = n - 1
able = 1
for i in range(n):
    if land[i] == 1:
        start = i
        break
    if i == n-1:
        able = 0
        print(0)
if able:
    for i in range(n-1, -1, -1):
        if land[i] == 1:
            end = i
            break
    for i in range(start, end):
        if land[i] == 0:
            if land[i-1] != 9 and land[i+1] != 9:
                count += 1
    print(count)
