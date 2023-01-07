n, s = [int(i) for i in input().split()]
level = s // 1000
maxid = 0; maxcp = 0
for i in range(1, n+1):
    cp, iv = [int(k) for k in input().split()]
    x = 0
    if iv >= 40:
        x = cp + 100*level
    elif iv >= 30:
        x = cp + 50*level
    else:
        x = cp + 10*level
    if x > maxcp:
        maxcp = x
        maxid = i
print(maxid, maxcp)