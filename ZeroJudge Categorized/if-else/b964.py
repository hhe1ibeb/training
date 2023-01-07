n = int(input())
score = [int(i) for i in input().split(' ')]
score.sort()
for i in score:
    print(i, end=' ')
print()
for i in range(1, n + 1):
    if score[-i] < 60:
        print(score[-i])
        break
    if i == n:
        print('best case')
for i in range(n):
    if score[i] > 60:
        print(score[i])
        break
    if i == n - 1:
        print('worst case')