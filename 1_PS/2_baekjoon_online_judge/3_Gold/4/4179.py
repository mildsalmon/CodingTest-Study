"""
Date    : 2022.03.17
Update  : 2022.03.17
Source  : 4179.py
Purpose : bfs
url     : https://www.acmicpc.net/problem/4179
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
from collections import deque
import sys

input = sys.stdin.readline


def move(j_q: deque, j_visited: list, fire_q: deque, fire_visited: list) -> int:
    global miro, r, c

    ds = ((1, 0), (0, 1), (-1, 0), (0, -1))

    while fire_q:
        # 불 -> 지훈 이동
        x, y = fire_q.popleft()

        for d in ds:
            fdx = x + d[0]
            fdy = y + d[1]

            if 0 <= fdx < r and 0 <= fdy < c:
                if fire_visited[fdx][fdy] == -1 and miro[fdx][fdy] != '#':
                    fire_visited[fdx][fdy] = fire_visited[x][y] + 1
                    fire_q.append((fdx, fdy))

    # print(*fire_visited, sep='\n')

    while j_q:
        # 지훈
        x, y = j_q.popleft()

        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx < r and 0 <= dy < c:
                if j_visited[dx][dy] == -1 and miro[dx][dy] != '#':
                    j_visited[dx][dy] = j_visited[x][y] + 1

                    if fire_visited[dx][dy] > j_visited[dx][dy]:
                        j_q.append((dx, dy))
            else:
                return j_visited[x][y] + 1

    # print(*j_visited, sep='\n')

    return -1


if __name__ == "__main__":
    r, c = list(map(int, input().split()))
    miro = []
    j_q = deque()
    fire_q = deque()
    j_visited = [[-1 for _ in range(c)] for _ in range(r)]
    fire_visited = [[-1 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        temp = list(input())
        miro.append(temp)

        for j in range(c):
            if temp[j] == 'J':
                j_q.append((i, j))
                j_visited[i][j] = 0
            elif temp[j] == 'F':
                fire_q.append((i, j))
                fire_visited[i][j] = 0

    time = move(j_q, j_visited, fire_q, fire_visited)

    if time == -1:
        print("IMPOSSIBLE")
    else:
        print(time)