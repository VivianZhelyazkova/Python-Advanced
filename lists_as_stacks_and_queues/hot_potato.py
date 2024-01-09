from collections import deque

kids_names = deque(input().split())
toss = int(input()) - 1
# toss_counter = 0
#
# while len(kids_names) > 1:
#     leaver = kids_names.popleft()
#     toss_counter += 1
#     if toss_counter == toss:
#         print(f"Removed {leaver}")
#         toss_counter = 0
#     else:
#         kids_names.append(leaver)
#
# print(f"Last is {"".join(kids_names)}")

while len(kids_names) > 1:
    kids_names.rotate(-toss)
    leaver = kids_names.popleft()
    print(f"Removed {leaver}")

print(f"Last is {kids_names.popleft()}")
