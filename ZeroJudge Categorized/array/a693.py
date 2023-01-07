from itertools import accumulate


try:
    while True:
        n, m = [int(i) for i in input().split(' ')]
        food = [int(j) for j in input().split(' ')]
        foodSum = [0] + list(accumulate(food))
        for k in range(m):
            l, r = [int(a) for a in input().split(' ')]
            print(foodSum[r] - foodSum[l - 1])
except EOFError:
    pass