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

def move_ball(x, y, d):
    global graph

    count = 0

    while graph[x + d[0]][y + d[1]] != '#' and graph[x][y] != 'O':
        x += d[0]
        y += d[1]
        count += 1

    return x, y, count

def bfs(graph, red_ball, blue_ball):
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
            break
        else:
            move += 1

        for d in ds:
            dr_x, dr_y, r_c = move_ball(r_x, r_y, d)
            db_x, db_y, b_c = move_ball(b_x, b_y, d)

            if graph[db_x][db_y] != 'O':
                if graph[dr_x][dr_y] == 'O':
                    return True

                if dr_x == db_x and dr_y == db_y:
                    if r_c > b_c:
                        dr_x -= d[0]
                        dr_y -= d[1]
                    elif r_c < b_c:
                        db_x -= d[0]
                        db_y -= d[1]

                if (dr_x, dr_y, db_x, db_y) not in visited:
                    visited.add((dr_x, dr_y, db_x, db_y))
                    q.append((dr_x, dr_y, db_x, db_y, move))

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
        graph.append(temp)

    if bfs(graph, red_ball, blue_ball):
        print(1)
    else:
        print(0)
