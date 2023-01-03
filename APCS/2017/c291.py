n = int(input())
friends = list(map(int, input().split()))
start = 0
labeled = [0]*n
count = 0
while True:
    labeled[start] = 1
    nxt = friends[start]
    while start != nxt:
        labeled[nxt] = 1
        nxt = friends[nxt]
    count += 1
    for i in range(start+1, n):
        if labeled[i] == 0:
            start = i
            break
    else:
        print(count)
        break
