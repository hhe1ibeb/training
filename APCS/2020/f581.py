n, m = map(int, input().split())
rooms = list(map(int, input().split()))
mission = list(map(int, input().split()))

for i in range(n-1):
    rooms[i+1] = rooms[i]+rooms[i+1]
print(rooms)
# now = 0
# s = 0
# for target in mission:
#     while s < target:
#         s += rooms[now]
#         now = (now+1) % n
#     s = 0
# print(now)
