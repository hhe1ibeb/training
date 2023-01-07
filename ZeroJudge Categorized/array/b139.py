l, m = [int(i) for i in input().split(' ')]
trees = []
for i in range(l + 1):
    trees.append(1)
for i in range(m):
    a, b = [int(i) for i in input().split(' ')]
    for j in range(a, b + 1):
        trees[j] = 0
print(trees.count(1))