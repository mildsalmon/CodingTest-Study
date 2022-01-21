"""
Date    : 2022.01.22
Update  : 2022.01.22
Source  : 13459.py
Purpose : 구현 / 그래프 / BFS
url     : https://www.acmicpc.net/problem/13459
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from collections import deque


def move_ball(x: int, y: int, d: tuple) -> iter:
    global board

    count = 0

    while board[x+d[0]][y+d[1]] != '#' and board[x][y] != 'O':
        x += d[0]
        y += d[1]
        count += 1

    return x, y, count


def bfs(blue_ball: list, red_ball: list, board: list) -> int:
    ds = ((0, 1), (0, -1), (1, 0), (-1, 0))

    balls = blue_ball + red_ball
    time = 0

    q = deque()
    q.append(balls + [time])

    visited = set()
    visited.add(tuple(balls))

    while q:
        blue_x, blue_y, red_x, red_y, time = q.popleft()

        if time >= 10:
            continue

        time += 1

        for d in ds:
            blue_dx, blue_dy, blue_count = move_ball(blue_x, blue_y, d)
            red_dx, red_dy, red_count = move_ball(red_x, red_y, d)

            if board[blue_dx][blue_dy] != 'O':
                if board[red_dx][red_dy] == 'O':
                    return 1

                if blue_dx == red_dx and blue_dy == red_dy:
                    if blue_count > red_count:
                        blue_dx -= d[0]
                        blue_dy -= d[1]
                    elif blue_count < red_count:
                        red_dx -= d[0]
                        red_dy -= d[1]

                temp_visited = (blue_dx, blue_dy, red_dx, red_dy)
                if temp_visited not in visited:
                    visited.add(temp_visited)
                    q.append(list(temp_visited) + [time])
    return 0


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    board = []

    for i in range(n):
        temp = list(input())

        for j in range(m):
            if temp[j] == "B":
                blue_ball = [i, j]
            elif temp[j] == "R":
                red_ball = [i, j]
        board.append(temp)

    print(bfs(blue_ball, red_ball, board))