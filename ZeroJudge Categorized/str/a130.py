n = int(input())
for i in range(1, n):
    urlList = []; level = []
    for j in range(10):
        url, lev = input().split(' ')
        urlList.append(url)
        level.append(int(lev))
    print('Case #%d:' % i)
    if level.count(max(level)) > 1:
        for j in range(level.count(max(level))):
            print(urlList[level.index(max(level))])
            level[level.index(max(level))] = 0
    else:
        print(urlList[level.index(max(level))])