t = int(input())
for i in range(t):
    team = input(); jud = input()
    if ' ' in team:
        print('Case %d: Output Format Error' % (i+1))
    else:
        nsTeam = team.replace(' ', '')
        nsJud = team.replace(' ', '')
        if nsTeam != nsJud or team != jud:
            print('Case %d: Wrong Answer' % (i+1))
        else:
            print('Case %d: Yes' % (i+1))