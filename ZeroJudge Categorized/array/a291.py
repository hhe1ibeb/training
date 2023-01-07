try:
    while True:
        password = [int (a) for a in input().split(' ')]
        n = int(input())
        for i in range(n):
            inp = [int(b) for b in input().split(' ')]
            p = 0; q = 0
            for j in range(4):
                if password.count(inp[j]) > 0:
                    if inp[j] == password[j]:
                        p += 1
                    elif password.count(inp[j]) == inp.count(inp[j]):
                        q += 1
            print('%dA%dB' % (p, q))
except EOFError:
    pass