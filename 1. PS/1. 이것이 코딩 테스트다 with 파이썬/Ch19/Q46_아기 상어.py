# from collections import deque
#
# n = int(input())
#
# space = []
# fish = []
# shark = []
# shark_size = 2
# shark_eat = 0
#
# for i in range(n):
#     temp = list(map(int, input().split()))
#     space.append(temp)
#
#     for j in range(n):
#         if temp[j] != 0 and temp[j] != 9:
#             fish.append((temp[j], i, j))
#         elif temp[j] == 9:
#             shark = [i, j]
#
# fish.sort()
#
# q = deque()
#
# for i in range(len(fish)):
#     if shark_size > fish[i][0]:
#         temp = fish[i]
#         q.append(temp)
#
# ds = ((1, 0), (-1, 0), (0, 1), (0, -1))
# time = 0
#
# while q:
#     fish_num, fish_x, fish_y = q.popleft()
#     shark_x, shark_y = shark
#     distance = abs(shark_x - fish_x) + abs(shark_y - fish_y)
#     # print(distance)
#     time += distance
#     shark[0], shark[1] = fish_x, fish_y
#     shark_eat += 1
#
#     if shark_eat == shark_size:
#         fish.sort(key=lambda x:[x[2], x[1]])
#         shark_size += 1
#         shark_eat = 0
#         new_fish = []
#
#         for i in range(len(fish)):
#             if shark_size-1 == fish[i][0]:
#                 temp = [abs(shark[0] - fish[i][1]) + abs(shark[1] - fish[i][2])] + list(fish[i])
#                 new_fish.append(temp)
#
#         new_fish.sort(key=lambda x:x[0])
#
#         for new in new_fish:
#             q.append(new[1:])
#
# print(time)

from collections import deque

n = int(input())

space = []
fish = []
shark = []
shark_size = 2
shark_eat = 0

for i in range(n):
    temp = list(map(int, input().split()))
    space.append(temp)

    for j in range(n):
        if temp[j] != 0 and temp[j] != 9:
            fish.append((temp[j], i, j))
        elif temp[j] == 9:
            shark = [i, j]

fish.sort()

q = deque()

for i in range(len(fish)):
    if shark_size > fish[i][0]:
        temp = fish[i]
        q.append(temp)

time = 0

def dfs(space, temp_space, shark_x, shark_y, fish_x, fish_y, shark_size, time, result):
    ds = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for d in ds:
        shark_dx = shark_x + d[0]
        shark_dy = shark_y + d[1]

        dist_temp = abs(shark_dx - fish_x) + abs(shark_dy - fish_y)

        if 0 <= shark_dx < len(space) and 0 <= shark_dy < len(space):
            if space[shark_dx][shark_dy] <= shark_size:
                if not temp_space[shark_dx][shark_dy]:
                    time += 1
                    # print(*space, sep='\n')
                    # print()
                    # print(*temp_space, sep='\n')
                    # print()
                    if fish_x == shark_dx and fish_y == shark_dy:
                        result.append(time)
                        # print(time)
                        # space[shark_dx][shark_dy]
                        temp_space[shark_dx][shark_dy] = False
                        break
                    else:
                        space[shark_dx][shark_dy] = 9  ###
                        temp_space[shark_dx][shark_dy] = True
                        dfs(space, temp_space, shark_dx, shark_dy, fish_x, fish_y, shark_size, time, result)
                        temp_space[shark_dx][shark_dy] = False
                        space[shark_dx][shark_dy] = 0
                        time -= 1
    # print("----")
    # return time

def bfs(temp_space, shark_x, shark_y, fish_x, fish_y, shark_size, time):
    b_q = deque()
    b_q.append((shark_x, shark_y))

    ds = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while b_q:
        x, y = b_q.popleft()

        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx < len(temp_space) and 0 <= dy < len(temp_space):
                if temp_space[dx][dy] <= shark_size:
                    temp_space[dx][dy] = temp_space[x][y] + 1  ###

                    if dx == fish_x and dy == fish_y:
                        return temp_space[fish_x][fish_y]
                    else:
                        # temp_space[dx][dy] = time
                        b_q.append((dx, dy))
                    print(*temp_space, sep='\n')
                    print()
                    print(dx, dy)

    return 0

while q:
    print("Q: ", q)
    print("eat: ", shark_eat)
    print("size: ", shark_size)
    print("shark: ", shark)
    print("time: ", time)
    print("============")
    fish_num, fish_x, fish_y = q.popleft()
    shark_x, shark_y = shark

    while shark_x != fish_x or shark_y != fish_y:
        temp_space = [i[:] for i in space]
        result = []
        visited = [[False] * len(space) for _ in space]
        # print(temp_space)
        visited[shark_x][shark_y] = True
        temp_space[shark_x][shark_y] = 0
        # dfs(temp_space, visited, shark_x, shark_y, fish_x, fish_y, shark_size, 0, result)
        distance = bfs(temp_space, shark_x, shark_y, fish_x, fish_y, shark_size, 0)

        space[shark_x][shark_y] = 0
        space[fish_x][fish_y] = 9
        # result.sort()
        # distance = result[0]
        shark_x = fish_x
        shark_y = fish_y
        # print(result)

    # distance = abs(shark_x - fish_x) + abs(shark_y - fish_y)
    # print(distance)
    time += distance
    shark[0], shark[1] = fish_x, fish_y
    shark_eat += 1

    if shark_eat == shark_size:
        fish.sort(key=lambda x:[x[2], x[1]])
        shark_size += 1
        shark_eat = 0
        new_fish = []

        for i in range(len(fish)):
            if shark_size-1 == fish[i][0]:
                temp = [abs(shark[0] - fish[i][1]) + abs(shark[1] - fish[i][2])] + list(fish[i])
                new_fish.append(temp)

        new_fish.sort(key=lambda x:x[0])

        for new in new_fish:
            q.append(new[1:])

print(time)