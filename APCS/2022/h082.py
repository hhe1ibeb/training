n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
idx = list(map(int, input().split()))
res = [0]*n
while len(idx) > 1:
    remidx = []
    for i in range(1, len(idx), 2):
        a, c = s[i-1:i+1]
        b, d = t[i-1:i+1]
        if a*b >= c*d:
            res[i] += 1
            if res[i] >= m:
                remidx.append(i)
            else:
                s[i] = a+c*d/(2*b)
                t[i] = b+c*d/(2*a)
                s[i-1] = c+c/2
                t[i-1] = d+d/2
        else:
            res[i-1] += 1
            if res[i-1] >= m:
                remidx.append(i-1)
            else:
                s[i-1] = a+c*d/(2*b)
                t[i-1] = b+c*d/(2*a)
                s[i] = c+c/2
                t[i] = d+d/2
    for i in remidx[::-1]:
        s.pop(i)
        t.pop(i)
        idx.pop(i)
        res.pop(i)
    print(res)
print(idx)
