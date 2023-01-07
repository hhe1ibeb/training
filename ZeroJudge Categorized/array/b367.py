t = int(input())
for k in range(t):
    n, m = [int(i) for i in input().split(' ')]
    arr = []
    for i in range(n):
        nums = input().split(' ')
        for each in nums:
            arr.append(each)
    if arr == arr[::-1]:
        print('go forward')
    else:
        print('keep defending')
