"""
Date    : 2022.03.17
Update  : 2022.03.20
Source  : 4179.py
Purpose : bfs
url     : https://www.acmicpc.net/problem/4179
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
from collections import deque


def move(jihun, fires, f_miro, j_miro):
    global r, c, miro

    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

    while fires:
        x, y = fires.popleft()

        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx < r and 0 <= dy < c:
                if miro[dx][dy] == '#':
                    continue
                if f_miro[dx][dy] == -1:
                    f_miro[dx][dy] = f_miro[x][y] + 1
                    fires.append((dx, dy))

    # print(*f_miro, sep='\n')

    while jihun:
        x, y = jihun.popleft()

        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx < r and 0 <= dy < c:
                if miro[dx][dy] == '#':
                    continue
                if j_miro[dx][dy] == -1:
                    j_miro[dx][dy] = j_miro[x][y] + 1
                    if f_miro[dx][dy] == -1 or j_miro[dx][dy] < f_miro[dx][dy]:
                        jihun.append((dx, dy))
            else:
                return j_miro[x][y] + 1
    return -1

if __name__ == "__main__":
    r, c = list(map(int, input().split()))
    miro = []
    jihun = deque()
    fires = deque()
    f_miro = [[-1 for _ in range(c)] for i in range(r)]
    j_miro = [[-1 for _ in range(c)] for i in range(r)]

    for i in range(r):
        temp = list(input())

        for j in range(c):
            if temp[j] == 'J':
                jihun.append((i, j))
                j_miro[i][j] = 0
            elif temp[j] == 'F':
                fires.append((i, j))
                f_miro[i][j] = 0
        miro.append(temp)

    time = move(jihun, fires, f_miro, j_miro)

    if time == -1:
        print("IMPOSSIBLE")
    else:
        print(time)