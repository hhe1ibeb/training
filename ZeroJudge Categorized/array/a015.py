try:
    while True:
        row, column = [int(i) for i in input().split(' ')]
        arr = []
        for i in range(row):
            arr.append([int(i) for i in input().split(' ')])
        for i in range(column):
            for j in range(row):
                print(arr[j][i], end=' ')
            print()
except EOFError:
    pass