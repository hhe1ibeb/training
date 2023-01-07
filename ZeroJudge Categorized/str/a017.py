try:
    while True:
        inp = input().replace('/', '//')
        print(eval(inp))
except EOFError:
    pass