n = int(input())
img = []
for i in range(n):
    img.append(list(map(int, input().split())))

img_arr = []

for i in range(n//2):
    for j in range(n//2):
        img_arr.append(img[i][j])

print(img_arr)
