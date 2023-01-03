n, d = map(int, input().split())
a = list(map(int, input().split()))
now = a[0]
last = 0
s = 0
for each in a[1::]:
    if now != 0:
        if each >= now + d:
            last = each
            s += each - now
            now = 0
    elif each <= last - d:
        now = each
print(s)
