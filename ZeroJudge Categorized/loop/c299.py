inp = [int(i) for i in input().split(' ')]
n = inp[0]
m = inp[1::]
m.sort()
s = str(m[0]) + ' ' + str(m[len(m) - 1]) + ' '; isNext = True
for j in range(len(m)):
    if j != 0:
        if m[j] - m[j-1] == 1:
            pass
        else:
            isNext = False
            break
if isNext:
    print('%syes' % s)
else:
    print('%sno' % s)