import collections
n = int(input())
for i in range(n):
    inp = list(input())
    freq = collections.Counter(inp)
    a = list(freq.values())
    maxValue = max(freq.values())
    str = ''
    if a.count(maxValue) > 1:
        for j in range(a.count(maxValue)):
            str += inp[max(freq.values())]
            inp.remove(inp[max(freq.values())])
    else:
        print(inp[max(freq.values())])