from collections import deque

n = int(input())
k = int(input())

board = [[0] * n for i in range(n)]

apple = []

for i in range(k):
    temp = list(map(int, input().split()))
    temp = [temp[0] - 1, temp[1] -1]
    apple.append(temp)
    board[temp[0]][temp[1]] = 2

l = int(input())
snake_distance = deque()

for i in range(l):
    temp = list(input().split())
    snake_distance.append([int(temp[0]), temp[1]])
snake_distance.append([0, 'x'])

pre_distance = snake_distance.popleft()

time = 0

ds = ((0, 1), (1, 0), (0, -1), (-1, 0))
d_pos = 0
d = ds[d_pos]

snake_head = [0, 0]
snake_tail = deque()
snake_tail.append((0, 0))

board[0][0] = 1

while True:
    if time == pre_distance[0]:
        if pre_distance[1] == 'L':
            # 왼쪽
            d_pos = (d_pos - 1) % 4
        elif pre_distance[1] == 'D':
            # 오른쪽
            d_pos = (d_pos + 1) % 4
        d = ds[d_pos]
        pre_distance = snake_distance.popleft()

    time += 1

    x, y = snake_head

    dx = x + d[0]
    dy = y + d[1]

    if 0 <= dx < n and 0 <= dy < n:
        if board[dx][dy] != 1:
            snake_head = [dx, dy]
            if board[dx][dy] == 2:
                board[dx][dy] = 1
            elif board[dx][dy] != 2:
                sx, sy = snake_tail.popleft()
                board[sx][sy] = 0
            board[dx][dy] = 1
            snake_tail.append((dx, dy))

        elif board[dx][dy] == 1:
            break
    else:
        break

print(time)