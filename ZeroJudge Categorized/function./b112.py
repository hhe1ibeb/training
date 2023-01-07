import math

try:
    while True:
        n = int(input())
        teams = []; x = 1
        for i in range(n):
            teams.append(int(input()))
            if i > 0:
                if x != 1:
                    x = math.gcd(teams[i], x)
                else:
                    x = math.gcd(teams[i], teams[i-1])
        print(x)
except EOFError:
    pass