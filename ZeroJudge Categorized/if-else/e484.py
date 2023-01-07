a = int(input())
isPrime = True
for i in range(2, a//2+1):
    if a % i == 0:
        isPrime = False
        break
if isPrime or a==1: print('yes')
else: print('no')