import datetime
try:
    while True:
        a = [int(i) for i in input().split(' ')]
        a_days = datetime.datetime(a[0], a[1], a[2])

        b = [int(i) for i in input().split(' ')]
        b_days = datetime.datetime(b[0], b[1], b[2])

        print(abs((a_days - b_days).days))
except EOFError:
    pass