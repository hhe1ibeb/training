n = int(input())
h = [int(i) for i in input().split(' ')]
cost = 0
for i in range(n):
    if h[i] == 0:
        if i == 0:
            cost += h[1]
            h[i] == h[1]
        elif i == n - 1:
            cost += h[n - 2]
            h[i] == h[n - 2]
        else:
            if h[i-1] > h[i+1]:
                cost += h[i+1]
                h[i] = h[i+1]
            elif h[i-1] < h[i+1]:
                cost += h[i-1]
                h[i] = h[i-1]
            else:
                cost += h[i-1]
                h[i] = h[i-1]
print(cost)