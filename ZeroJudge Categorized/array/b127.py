try:
    while True:
        n = 0
        arr = []
        for i in range(46):
            arr.append(0)
        arr[1] = 1
        arr[2] = 2
        for i in range(3, 46):
            arr[i] = arr[i -1] + arr[i - 2]
        print(arr[int(input())])
except EOFError:
    pass