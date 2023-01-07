n = int(input())
for i in range(n):
    a, b, c = [int(j) for j in input().split(' ')]
    if a == 1:
        print(b + c)
    elif a == 2:
        print(b - c)
    elif a == 3:
        print(b * c)
    elif a == 4:
        print(b // c)