try:
    while True:
        arr = list(map(int, input().split()))
        n = len(arr)
        out = []
        for i in range(n):
            a = min(arr)
            arr.remove(a)
            out.append(a)
        print(out)
except EOFError:
    pass
