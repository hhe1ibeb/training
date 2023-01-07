n, m = [int(i) for i in input().split(' ')]
for i in range(n):
    arr1 = [int(i) for i in input().split(' ')]
    arr2 = [int(i) for i in input().split(' ')]
    print(len(list(set(arr1).intersection(arr2))))