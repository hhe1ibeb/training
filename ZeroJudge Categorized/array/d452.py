import statistics
try:
    while True:
        n = int(input())
        for i in range(n):
            x = 0
            inp = [int(i) for i in input().split(' ')]
            m = inp[0]; inp.remove(m)
            mid = statistics.median(inp)
            for j in inp:
                x += abs(mid - j)
            print(int(x))
except EOFError:
    pass