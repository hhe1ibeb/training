s1 = input()
while s1 != 'STOP!!':
    s1 = list(s1); s2 = list(input())
    a = 0; b = 0
    for i in s1:
        a += ord(i)
    for i in s2:
        b += ord(i)
    if a == b:
        print('yes')
    else:
        print('no')
    s1 = input()