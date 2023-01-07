n, m = [int(i) for i in input().split(' ')]
s = 0
nums = []
for i in range(n):
    k = max([int(k) for k in input().split(' ')])
    s += k
    nums.append(k)
print(s)
div = []
for i in nums:
    if s % i == 0:
        div.append(i)
if len(div) == 0:
    print(-1)
else:
    for i in range(len(div) - 1):
        print(div[i], end=' ')
    print(div[len(div)-1])