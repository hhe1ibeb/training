codeList = {'0 1 0 1' : 'A', '0 1 1 1' : 'B', '0 0 1 0' : 'C', '1 1 0 1' : 'D', '1 0 0 0' : 'E', '1 1 0 0' : 'F'}

try:
    while True:
        n = int(input())
        out = ''
        for i in range(n):
            s = input()
            out += codeList[s]
        print(out)
except EOFError:
    pass