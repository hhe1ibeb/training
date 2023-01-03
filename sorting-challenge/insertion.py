try:
    while True:
        arr = list(map(int, input().split()))
        n = len(arr)
        out = []
        for i in range(n):
            out.append(arr[i])
            a = arr[i+1]
            
except EOFError:
    pass