try:
    while True:
        print(bin(int(input()))[2::])
except EOFError:
    pass