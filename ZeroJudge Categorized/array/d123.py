case = 1
try:
    while True:
        n = int(input()); isB2 = True
        arr = [int(i) for i in input().split(' ')]
        sumArr = arr
        for j in range(n):
            if j == 0:
                if arr[j] < 1:
                    isB2 = False
                    break
            else:
                if arr[j] < arr[j-1]:
                    isB2 = False
                    break
                if sumArr.count(arr[j] + arr[j-1]) > 0:
                    isB2 = False
                    break
                else:
                    sumArr.append(arr[j] + arr[j-1])
                print(sumArr)
            print(j)

        if isB2:
            print('Case #%d: It is a B2-Sequence.' % case)
        else:
            print('Case #%d: It is not a B2-Sequence.' % case)

        print()
        case += 1
except EOFError:
    pass