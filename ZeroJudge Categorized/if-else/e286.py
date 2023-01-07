homeWin = 0; guestWin = 0
for i in range(2):
    home = sum([int(i) for i in input().split(' ')])
    guest = sum([int(i) for i in input().split(' ')])
    print('%d:%d' % (home, guest))
    if home > guest:
        homeWin += 1
    else:
        guestWin += 1
if homeWin > guestWin:
    print('Win')
elif homeWin < guestWin:
    print('Lose')
else:
    print('Tie')