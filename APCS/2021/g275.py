n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    isAC = True
    if (a[1] == a[3] or a[1] != a[5]) or (b[1] == b[3] or b[1] != b[5]):
        isAC = False
        print("A", end="")
    if (a[6] != 1 or b[6] != 0):
        isAC = False
        print("B", end="")
    if a[1] == b[1] or a[3] == b[3] or a[5] == b[5]:
        isAC = False
        print("C", end="")
    if isAC:
        print("None")
    print()
