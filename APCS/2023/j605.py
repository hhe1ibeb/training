k = int(input())
score = []
time = []
h = 0
bad = 0
for i in range(k):
    s = list(map(int, input().split()))
    if s[1] == -1:
        bad += 1
    if s[1] > h:
        h = s[1]
    time.append(s[0])
    score.append(s[1])
best = time[score.index(h)]
final = h - k - bad*2
if final < 0:
    print(0, best)
else:
    print(final, best)
