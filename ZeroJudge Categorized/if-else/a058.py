n = int(input())
a = [0, 0, 0]
for i in range(n):
    a[int(input())%3] += 1
print(a[0], a[1], a[2])