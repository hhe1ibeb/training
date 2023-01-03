try:
    while True:
        arr = [int(i) for i in input().split()]
        n = len(arr)
        for i in range(n):
            for j in range(i):
                if arr[i] < arr[j]:
                    a = arr[j]
                    arr[j] = arr[i]
                    arr[i] = a
        print(arr)
except EOFError:
    pass