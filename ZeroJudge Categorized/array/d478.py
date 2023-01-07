n, m = [int(i) for i in input().split(' ')]
for i in range(n):
    x = 0
    arr1 = [int(i) for i in input().split(' ')]
    arr2 = [int(i) for i in input().split(' ')]
    a = 0; b = 0
    while a < m and b < m:
        if arr1[a] == arr2[b]:
            x += 1
            a += 1; b += 1
        elif arr1[a] < arr2[b]:
            a += 1
        else:
            b += 1
    print(x)