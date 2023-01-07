n = int(input())
direction = int(input())
inputArray = []
for i in range(n):
    inputArray.append(input().split())
output = ''
x = y = (n-1)//2
output += inputArray[x][y]
d = direction
for i in range(1, n):
    for j in range(2):
        print(x, y)
        if d == 0:
            x -= 1
        if d == 1:
            y -= 1
        if d == 2:
            x += 1
        if d == 3:
            y += 1
        output += inputArray[x][y]
        if j == i - 1:
            if d == 3: d = 0
            else: d += 1
print(output)