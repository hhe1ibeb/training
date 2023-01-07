n = int(input())
arr = list(map(int, input().split()))
m = int(input())
for i in range(m):
    command = list(map(int, input().split()))
    if command[0] == 3:
        if arr.count(0) > 0:
            print(arr.index(0))
        else:
            print(-1)
    elif command[0] == 2:
        arr[command[1]] = 0
    else:
        if arr.count(0) > 0:
            index = arr.index(0)
            arr[index] = command[1]
