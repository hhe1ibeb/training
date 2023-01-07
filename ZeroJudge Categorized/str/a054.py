letters = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,
            'J':18,'K':19,'L':20,'M':21,'N':22,'O':35,'P':23,'Q':24,'R':25,
            'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33}
n = [int(i) for i in list(input())]
s = 0
for j in range(8):
    s += n[j] * (8 - j)
out = ''
for k in letters:
    a = letters[k] // 10 ; b = letters[k] % 10
    if n[8] == 0:
        if (s + a + b * 9) % 10 == 0:
            out += k
    elif n[8] == 10 - (s + a + b * 9) % 10 :
        out += k
print(out)