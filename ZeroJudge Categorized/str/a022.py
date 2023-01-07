from pprint import isreadable


inp = input()
l = len(inp); n = 0; isReverse = True
if l % 2 == 0:
    n = l // 2
else:
    n = (l - 1) // 2
for i in range(n):
    if inp[i] == inp[l - i - 1]:
        pass
    else:
        isReverse = False
        break
if isReverse:
    print('yes')
else:
    print('no')