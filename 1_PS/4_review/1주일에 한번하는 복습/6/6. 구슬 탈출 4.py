"""
Date    : 2022.01.22
Update  : 2022.01.22
Source  : 15653.py
Purpose : 구현 / 그래프 / BFS
url     : https://www.acmicpc.net/problem/15653
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from collections import deque


def move_ball(x: int, y: int, d: list) -> iter:
    global board

    count = 0

    while board[x+d[0]][y+d[1]] != '#' and board[x][y] != 'O':
        x += d[0]
        y += d[1]
        count += 1

    return x, y, count


def bfs(blue_x: int, blue_y: int, red_x: int, red_y: int) -> int:
    global board

    ds = ((0, 1), (0, -1), (1, 0), (-1, 0))

    q = deque()
    q.append((blue_x, blue_y, red_x, red_y, 0))

    visited = set()
    visited.add((blue_x, blue_y, red_x, red_y))

    while q:
        b_x, b_y, r_x, r_y, time = q.popleft()

        time += 1

        for d in ds:
            b_dx, b_dy, b_c = move_ball(b_x, b_y, d)
            r_dx, r_dy, r_c = move_ball(r_x, r_y, d)

            if board[b_dx][b_dy] != 'O':
                if board[r_dx][r_dy] == 'O':
                    return time

                if b_dx == r_dx and b_dy == r_dy:
                    if b_c > r_c:
                        b_dx -= d[0]
                        b_dy -= d[1]
                    elif b_c < r_c:
                        r_dx -= d[0]
                        r_dy -= d[1]

                temp_visited = (b_dx, b_dy, r_dx, r_dy)

                if temp_visited not in visited:
                    visited.add(temp_visited)
                    q.append(list(temp_visited) + [time])

    return -1


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    board = []

    for i in range(n):
        temp = list(input())

        for j in range(m):
            if temp[j] == 'B':
                blue_x, blue_y = i, j
            elif temp[j] == 'R':
                red_x, red_y = i, j
        board.append(temp)

    print(bfs(blue_x, blue_y, red_x, red_y))