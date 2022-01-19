"""
Date    : 2022.01.19
Update  : 2022.01.19
Source  : 15653.py
Purpose :
url     : https://www.acmicpc.net/problem/15653
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys
from collections import deque

input = sys.stdin.readline

def move_ball(x, y, d):
    global graph

    count = 0

    while graph[x+d[0]][y+d[1]] != '#' and graph[x][y] != 'O':
        x += d[0]
        y += d[1]
        count += 1

    return x, y, count

def bfs(red_x, red_y, blue_x, blue_y):
    global graph

    ds = ((0, 1), (0, -1), (1, 0), (-1, 0))

    q = deque()
    q.append((red_x, red_y, blue_x, blue_y, 0))

    visited = set()
    visited.add((red_x, red_y, blue_x, blue_y))

    while q:
        r_x, r_y, b_x, b_y, time = q.popleft()

        for d in ds:
            r_dx, r_dy, r_count = move_ball(r_x, r_y, d)
            b_dx, b_dy, b_count = move_ball(b_x, b_y, d)

            if graph[b_dx][b_dy] != 'O':
                if graph[r_dx][r_dy] == 'O':
                    return time + 1

                if r_dx == b_dx and r_dy == b_dy:
                    if r_count > b_count:
                        r_dx -= d[0]
                        r_dy -= d[1]
                    elif r_count < b_count:
                        b_dx -= d[0]
                        b_dy -= d[1]

                balls = (r_dx, r_dy, b_dx, b_dy)

                if balls not in visited:
                    visited.add(balls)
                    q.append(list(balls) + [time+1])

    return -1

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    graph = []

    for i in range(n):
        temp = list(input().rstrip())

        for j in range(m):
            if temp[j] == 'B':
                blue_x, blue_y = i, j
            elif temp[j] == 'R':
                red_x, red_y = i, j
            elif temp[j] == 'O':
                hole_x, hole_y = i, j

        graph.append(temp)

    print(bfs(red_x, red_y, blue_x, blue_y))