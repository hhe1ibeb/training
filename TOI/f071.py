nums = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
money = 0

double = 1
for i in range(3):
    for j in range(5):
        x = nums[i]
        if A[j] == x:
            if i < 2:
                money += B[j]
            else:
                double = 0
                money -= B[j]

if double:
    money *= 2

if money < 0:
    print(0)
else:
    print(money)
