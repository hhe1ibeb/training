a = []
b = []
for i in range(3):
    x = list(map(int, input().split()))
    a.append(x[0])
    b.append(x[1])

n = max(a)
k = b[a.index(n)]
i = 1
m = n*i + k
b.pop(a.index(n))
a.remove(n)
while True:
    m = n*i + k
    passed = 1
    for j in range(2):
        if m % a[j] != b[j]:
            passed = 0
            break
    if passed:
        break
    i += 1
print(m)
