a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
n = int(input())
total = []
for i in range(n+1):
    x1 = i
    x2 = n - x1
    y1 = a1*(x1**2) + b1*x1 + c1
    y2 = a2*(x2**2) + b2*x2 + c2
    total.append(y1+y2)
print(max(total))
