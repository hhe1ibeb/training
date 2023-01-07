def isReverse(a):
    if str(a) == str(a)[::-1]:
        return True
    return False

n = int(input())
for i in range(n):
    count = 0
    p = int(input()); q = int(str(p)[::-1])
    while isReverse(p + q) == False:
        p = p + q; q = int(str(p)[::-1])
        count += 1
    print('%d %d' % (count+1, p + q))