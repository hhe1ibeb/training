n, m, k = [int(i) for i in input().split(' ')]
members = []
for i in range(1, n+1):
    members.append(i)
for i in range(k):
    if len(members) > m:
        a