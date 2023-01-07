x = int(input())
pas = []

print(1)
for k in range(1, x+1):
  arr = []
  for i in range(k+1):
    a = 0
    if k == 2 and i == 1:
      a = 2
    elif k == 1 or i == 0 or i == k:
      a = 1
    else:
      a = pas[k-2][i-1] + pas[k-2][i]
    arr.append(a)
    print(a, end=' ')
  pas.append(arr)
  print()