m, n = map(int, input().split())
s = list(map(int, input().split()))
count = 0
for i in range(n-m+1):
    x = s[i:i+m]
    isdiffer = 1
    for j in range(m-1):
        if x.count(x[j]) > 1:
            isdiffer = 0
    if isdiffer:
        count += 1
print(count)
