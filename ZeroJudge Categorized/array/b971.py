a1, an, d = map(int, input().split())
print(a1, end=' ')
for i in range((an-a1)//d):
    a1 += d
    print(a1, end=' ')