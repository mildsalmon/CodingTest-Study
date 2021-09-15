# 백준 3190번 문제

from collections import deque

n = int(input())

game_map = [[0] * (n+1) for _ in range(n+1)]

apple_count = int(input())
apple_pos = []
for i in range(apple_count):
    # apple_pos.append(list(map(int, input().split())))
    x, y = list(map(int, input().split()))
    game_map[x][y] = 2

snake_d_count = int(input())
# snake_d_info = deque()
snake_d_info = []
for i in range(snake_d_count):
    temp = list(input().split())
    # snake_d_info.append([int(temp[0]), temp[1]])
    snake_d_info.append([int(temp[0]), temp[1]])
d = 0

ds = [(0,1), (1,0), (0,-1), (-1,0)]

pos = [1, 1]
snake_length = 1
time = 0

q_head_pos = deque()
q_head_pos.append(pos)

q_tail_pos = deque()
q_tail_pos.append(pos)

# game_map[pos[0]][pos[1]] = 1
# d_info_time, d_info_move = snake_d_info.popleft()

game_map[pos[0]][pos[1]] = 1
snake_d_info_point = 0

while True:
    x, y = q_head_pos.popleft()

    if len(snake_d_info) > snake_d_info_point:
        if time == snake_d_info[snake_d_info_point][0]:
            if snake_d_info[snake_d_info_point][1] == "D":
                d = (d + 1) % 4

            else:
                d = (d - 1) % 4
            # d_info_time, d_info_move = snake_d_info.popleft()
            snake_d_info_point += 1

    # if [x, y] in snake_d_info:
    #     if

    time += 1

    dx = x + ds[d][0]
    dy = y + ds[d][1]

    if dx < 1 or dx > n or dy < 1 or dy > n:
        break

    if game_map[dx][dy] == 1:
        break


    if game_map[dx][dy] != 2:
        tx, ty = q_tail_pos.popleft()
        game_map[tx][ty] = 0

    game_map[dx][dy] = 1

    q_head_pos.append([dx, dy])
    q_tail_pos.append([dx, dy])

print(time)

# 1시간 45분 / Pass