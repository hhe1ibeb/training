def result(a, b):
    if a == b:
        return 0
    elif (a == 0 and b == 2) or (a == 2 and b == 5) or (a == 5 and b == 0):
        return 1
    else:
        return 2


def opp(a):
    if a == 0:
        return 5
    elif a == 2:
        return 0
    else:
        return 2


f = int(input())
n = int(input())
y = list(map(int, input().split()))

for i in range(n):
    if i != 0:
        if i > 1:
            if y[i-1] == y[i-2]:
                f = opp(y[i-1])
            else:
                f = y[i-1]
        else:
            f = y[i-1]
    print(f, end=' ')
    res = result(f, y[i])
    if res == 1:
        print(': Won at round %d' % (i+1))
        break
    elif res == 2:
        print(': Lost at round %d' % (i+1))
        break
    elif i == n - 1:
        print(': Drew at round %d' % (i+1))
