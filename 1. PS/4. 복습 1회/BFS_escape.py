from collections import deque

n, m = list(map(int, input().split()))
game_map = []

for i in range(n):
    game_map.append(list(map(int, input())))

ds = ((0, -1), (1, 0), (0, 1), (-1, 0))

pos = deque()
pos.append([0,0])

while pos:
    x, y = pos.popleft()
    count = 0

    for j in range(4):
        dx = x + ds[j][0]
        dy = y + ds[j][1]

        if dx < 0 or dx >= n or dy < 0 or dy >= m:
            continue

        if game_map[dx][dy] == 0:
            continue

        if game_map[dx][dy] == 1:
            pos.append([dx, dy])
            game_map[dx][dy] = game_map[x][y] + 1
            count = count + 1
    if count <= 1:
        game_map[x][y] == 1

    if game_map[n-1][m-1] != 1:
        break

print(game_map[n-1][m-1])