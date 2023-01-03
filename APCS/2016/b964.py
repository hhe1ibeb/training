n = int(input())
grades = [int(i) for i in input().split(' ')]
grades.sort()
passed = []
fail = []
for each in grades:
    print(each, end=' ')
    if each >= 60:
        passed.append(each)
    else:
        fail.append(each)
print()
if len(fail) == 0:
    print('best case')
else:
    print(max(fail))
if len(passed) == 0:
    print('worst case')
else:
    print(min(passed))
