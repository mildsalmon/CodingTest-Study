"""
Date    : 2021.12.09
Update  : 2021.12.09
Source  : Q46_아기 상어.py
Purpose : bfs를 이용하여 구현하는 문제인줄 알았는데.... 문제를 잘못이해해서 틀렸다.. 내 4시간..
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
# 물고기는 번호와 방향을 갖는다.
    # 방향을 45도 반시계로

# 초기

# 상어는 물고기를 먹고 물고기 방향으로 이동한다.
    # 물고기 먹고 빈칸 만들기

# 물고기도 움직임
    # 이동 x -> 상어가 있거나, 공간 밖
    # 번호가 작은 순서로 이동함.
    # 이동할 수 있을떄까지 45도 회전
    #이동 x면 이동 x
    # 다른 물고기칸으로 이동할떄는 서로 위치를 바꾸는 방식으로

# 물고기 이동 -> 상어 이동

# 상어
    # 방향에 있는 칸을 이동할 수 있고 한 번에 여러 칸을 이동할 수 있음
    # 물고기가 있는칸으로 이동하면, 물고기 먹고 물고기의 방향을 갖는다.
    # 지나가는 칸에 있는 물고기는 먹지 않음
    # 빈 칸으로는 이동하지 못함
        # 이동하던 중 칸이 없으면 집으로 돌아감 ==> 이거를 초기 시작위치인 0,0으로 돌아간다고 이해하고 풀었음

# 상어가 집으로 간 후에는 물고기가 다시 움직임 -> 반복

from collections import deque
import copy

# def bfs(x, y):
#     new_q = deque()
#     # 방향 좌표 먹은거 반환
#     d = ds[fishs[x][y][1]]
#     dx = x + d[0]
#     dy = y + d[1]
#
#     if 0 <= dx < n and 0 <= dy < n:
#         if fishs[dx][dy][0] != 0 and fishs[dx][dy][0] != 99:
def bfs(array, x, y):
    q = deque()
    # shark_eat = 0

    # shark_move = [0, 0, 0, 0]
    for i in range(1, n):
        d = ds[fishs[x][y][1]]
        dx = x + d[0] * i
        dy = y + d[1] * i

        if 0 <= dx < n and 0 <= dy < n:
            # 물고기가 없는칸 제외
            if fishs[dx][dy][0] != 0 and fishs[dx][dy][0] != 99:
                q.append((dx, dy))
        else:
            break

    if len(q) == 0:
        # 상어가 지금까지 먹은 먹이 합
        next_fish = [fishs[x][y][0], x, y, fishs[x][y][1]]
        # eat_fish = [x, y]

        return next_fish #, eat_fish

    next_fishs = []
    eat_fishs = []
    # temp_fishs = []

    while q:
        nx, ny = q.popleft()
        next_fish = bfs(nx, ny)

        next_fishs.append(next_fish)
        # temp_fishs.append(eat_fish)

    next_fish = next_fishs[0]

    for i in range(1, len(next_fishs)):
        if next_fishs[i][0] > next_fishs[i-1][0]:
            next_fish = next_fishs[i]

    next_fish[0] += fishs[x][y][0]
    fishs[next_fish[1]][next_fish[2]][0] = 0
    next_fish[1] = x
    next_fish[2] = y
    # eat_fishs.append(next_fish)

    return next_fish#, eat_fishs

n = 4

fishs = []

for i in range(n):
    temp = list(map(int, input().split()))

    fish = []
    for j in range(n):
        fish.append([temp[j*2], temp[j*2+1]-1])
    fishs.append(fish)

ds = ((-1, 0), # 상
      (-1, -1), # 대 (왼상)
      (0, -1), # 왼
      (1, -1), # 대 (왼하)
      (1, 0), # 하
      (1, 1), # 대 (오하)
      (0, 1), # 오
      (-1, 1)) # 대 (오상)

ds_len = len(ds)

shark_pos = (0, 0)
shark_direction = fishs[0][0][1]
shark_eat = 0
shark_eat += fishs[0][0][0]

while True:
    fishs[0][0][0] = 99 # 상어

    # 물고기 이동
    moved_fish = [False] * (n*n + 1)

    for k in range(1, n*n+1):
        for i in range(n):
            for j in range(n):
                if fishs[i][j][0] == k and not moved_fish[k]:
                    for dk in range(ds_len):
                        d = ds[(fishs[i][j][1] + dk) % ds_len]
                        dx = i + d[0]
                        dy = j + d[1]

                        if 0 <= dx < n and 0 <= dy < n:
                            if fishs[dx][dy][0] != 99:
                                fishs[i][j][1] = (fishs[i][j][1] + dk) % ds_len
                                fishs[i][j], fishs[dx][dy] = fishs[dx][dy], fishs[i][j]
                                moved_fish[k] = True
                                break

    # 상어 이동
    fishs[shark_pos[0]][shark_pos[1]][0] = 0  # 상어 이동 준비
    next_fish = bfs(shark_pos[0], shark_pos[1])
    fishs[shark_pos[0]][shark_pos[1]][1] = next_fish[3]
    # print(next_fish)
    shark_eat += next_fish[0]

    if next_fish[0] == 0 or (next_fish[1] == 0 and next_fish[2] == 0):
        print(shark_eat)
        break
    # q = deque()
    #
    # # shark_move = [0, 0, 0, 0]
    # for i in range(n):
    #     d = ds[shark_direction]
    #     dx = shark_pos[0] + d[0] * i
    #     dy = shark_pos[1] + d[1] * i
    #
    #     if 0 <= dx < n and 0 <= dy < n:
    #         # 물고기가 없는칸 제외
    #         if fishs[dx][dy][0] != 0 and fishs[dx][dy][0] != 99:
    #             q.append((dx, dy))
    #     else:
    #         break
    #
    # while q:
    #     x, y = q.popleft()
    #     bfs(x, y)
                # shark_move = max(shark_move, [fishs[dx][dy][0], fishs[dx][dy][1], dx, dy])
    # shark_eat += shark_move[0]
    # shark_pos = (shark_move[2], shark_move[3])
    # shark_direction = shark_move[1]
