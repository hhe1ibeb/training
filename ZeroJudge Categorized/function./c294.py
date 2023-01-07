inp = [int(i) for i in input().split(' ')]
inp.sort()
a = inp[0]; b = inp[1]; c = inp[2]
if a + b <= c:
    print('%d %d %d' % (a, b, c))
    print('No')
else:
    k = a**2 + b**2
    print('%d %d %d' % (a, b, c))
    if k < c**2:
        print('Obtuse')
    elif k > c**2:
        print('Acute')
    else:
        print('Right')