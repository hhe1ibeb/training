n = int(input())
for i in range(n):
    isLoop = True
    tracks = input().split(' ')
    if len(tracks) < 2:
            isLoop = False
    for j in range(len(tracks)):
        if j != len(tracks) - 1:
            if tracks[j][1] == tracks[j+1][0]:
                isLoop = False
        else:
            if tracks[j][1] == tracks[0][0]:
                isLoop = False
        if isLoop == False:
            break
    if isLoop:
        print('LOOP')
    else:
        print('NO LOOP')