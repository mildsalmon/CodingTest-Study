"""
Date    : 2022.01.18
Update  : 2022.01.18
Source  : 13459.py
Purpose :
url     : https://www.acmicpc.net/problem/13459
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, red_ball, blue_ball, hall, walls):
    ds = ((0, 1), (0, -1), (1, 0), (-1, 0))

    move = 0

    visited = set()
    balls = red_ball + blue_ball
    visited.add(tuple(balls))

    balls += [move]
    q = deque([balls])

    while q:
        r_x, r_y, b_x, b_y, move = q.popleft()

        if move >= 10:
            continue
        else:
            move += 1

        for d in ds:
            dr_x = r_x + d[0]
            dr_y = r_y + d[1]
            db_x = b_x + d[0]
            db_y = b_y + d[1]
            flag = True

            red_stop = False
            blue_stop = False

            red_hall_in = False
            blue_hall_in = False

            while flag:
                # if graph[dr_x][dr_y] == '#' and graph[db_x][db_y] == '#':
                if red_stop and blue_stop:
                    flag = False
                    if not(dr_x - d[0] == r_x and dr_y - d[1] == r_y):
                        dr_x -= d[0]
                        dr_y -= d[1]
                        db_x -= d[0]
                        db_y -= d[1]

                        if (dr_x, dr_y, db_x, db_y) not in visited:
                            visited.add((dr_x, dr_y, db_x, db_y))
                            q.append((dr_x, dr_y, db_x, db_y, move))
                else:
                    if dr_x == db_x and dr_y == db_y:
                        # 두 볼이 동시에 같은 방향으로 움직이면 절대 같은 좌표가 될 수 없다.
                        # 다만, 한개의 볼이 멈춰있을 경우에는 가능하다.
                        # 따라서, 두 볼의 좌표가 같은 경우에는 하나의 볼은 무조건 멈춰있다. 동시에 멈춰있을 수 없다.
                            # 그래서 elif 사용함.
                        if red_stop:
                            db_x -= d[0]
                            db_y -= d[1]
                            blue_stop = True
                        elif blue_stop:
                            dr_x -= d[0]
                            dr_y -= d[1]
                            red_stop = True

                        continue

                    if graph[dr_x][dr_y] != '#':
                        if graph[dr_x][dr_y] == 'O':
                            red_hall_in = True
                        dr_x += d[0]
                        dr_y += d[1]
                    else:
                        red_stop = True

                    if graph[db_x][db_y] != '#':
                        if graph[db_x][db_y] == 'O':
                            blue_hall_in = True
                        db_x += d[0]
                        db_y += d[1]
                    else:
                        blue_stop = True

            if blue_hall_in:
                return False
            if red_hall_in:
                return True

    return False

if __name__ == "__main__":
    n, m = list(map(int, input().split()))

    graph = []
    walls = set()

    for i in range(n):
        temp = list(input().rstrip())

        for j in range(m):
            if temp[j] == 'B':
                blue_ball = [i, j]
            elif temp[j] == 'R':
                red_ball = [i, j]
            elif temp[j] == 'O':
                hall = [i, j]
            elif temp[j] == '#':
                walls.add((i, j))
        graph.append(temp)

    if bfs(graph, red_ball, blue_ball, hall, walls):
        print(1)
    else:
        print(0)
