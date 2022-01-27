"""
Date    : 2022.01.27
Update  : 2022.01.27
Source  : 16954.py
Purpose : bfs / 메모이제이션
url     : https://www.acmicpc.net/problem/16954
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from collections import deque


def bfs(init_pos: list, walls_list: list) -> int:
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

        if stage >= chess_map_size:
            return 1

        # temp_walls = map_move(walls, stage)
        temp_walls = walls_list[stage]

        if (x, y) in temp_walls:
            continue

        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx < chess_map_size and 0 <= dy < chess_map_size:
                # if chess_map[dx][dy] == '.':
                if (dx, dy) not in temp_walls:
                    q.append([dx, dy, stage+1])

    return 0


def map_move(walls: set, stage: int) -> list:
    walls_list = [walls]

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
        walls_list.append(walls)

    return walls_list


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
    walls_list = map_move(walls, chess_map_size)

    print(bfs(init_pos, walls_list))

"""
다른 사람의 코드
시간이 광장히 짧아서 확인해봤는데, 와...
단순히 체스판을 그림그리듯이 True / False로 가능한 경로만 남기고 지우는 방식으로 해결하셨다.
이렇게도 할 수 있구나..
"""
#
# input = __import__('sys').stdin.readline
# a = [input() for _ in range(8)]  # 체스판
# d = [[False] * 8 for _ in range(8)]  # dp용 배열
# d[7][0] = True
# for i in range(8):  # 0초부터 7초까지 살펴봄
#
#     # -- 벽이 내려온 것을 다시 맞춰주는 작업-- --#
#     # 0초일 때는 사실상 필요 없음
#     for j in range(8 - i):
#         for k in range(8):  # (j+1,k+1) 포인트
#             if a[j][k] == '#':
#                 d[i + j][k] = False
#     # -- -- -- -- -- -- -- -- -- -- -- -- -- --#
#     td = [[False] * 8 for _ in range(8)]  # true check
#     # -- -- -- -- --케릭터가 갈 수 있는 곳을 True로 만들기-- -- -- --#
#     for j in range(8):
#         for k in range(8):
#             for x in range(-1, 2):
#                 for y in range(-1, 2):
#                     # 순서대로 - [5]가 현재 위치
#                     #  1 | 2 | 3
#                     # --- --- ---
#                     #  4 |[5]| 6
#                     # --- --- ---
#                     #  7 | 8 | 9
#
#                     if 0 <= j + x < 8 and 0 <= k + y < 8 and d[j + x][k + y]:
#                         td[j][k] = True
#     # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --#
#     for j in range(8 - i):
#         for k in range(8):
#             if a[j][k] == '#':
#                 td[i + j][k] = False
#     d = td
#     # print(f'{i} 초 후')
#     # [print(i) for i in td];print()
#
# print(1 if sum(map(sum, d)) else 0)