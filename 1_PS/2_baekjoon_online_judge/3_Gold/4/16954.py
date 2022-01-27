"""
Date    : 2022.01.27
Update  : 2022.01.27
Source  : 16954.py
Purpose :
url     : https://www.acmicpc.net/problem/16954
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from collections import deque


def bfs(init_pos, walls):
    global chess_map_size

    q = deque()
    q.append(init_pos + [0])

    ds = (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1)
    )

    while q:
        x, y, stage = q.popleft()

        if x == 0 and y == 7:
            return 1

        temp_walls = map_move(walls, stage)

        if (x, y) in temp_walls:
            continue

        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx < chess_map_size and 0 <= dy < chess_map_size:
                # if chess_map[dx][dy] == '.':
                if (dx, dy) not in temp_walls:
                    q.append([dx, dy, stage + 1])

    return 0


def map_move(walls, stage):
    for _ in range(stage):
        temp_walls = set()

        for wall in walls:
            x, y = wall
            x += 1

            if x >= chess_map_size:
                continue
            else:
                temp_walls.add((x, y))
        walls = temp_walls

    return walls


if __name__ == "__main__":
    chess_map_size = 8
    chess_map = []
    walls = set()

    for i in range(chess_map_size):
        temp = list(input())
        chess_map.append(temp)

        for j in range(chess_map_size):
            if temp[j] == "#":
                walls.add((i, j))

    init_pos = [7, 0]

    print(bfs(init_pos, walls))

