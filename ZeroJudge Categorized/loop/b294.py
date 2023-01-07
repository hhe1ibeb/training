n = int(input())
count = [int(i) for i in input().split(' ')]
cost = 0
for i in range(1, n+1):
    cost += count[i-1] * i
print(cost)