"""
Date    : 2022.03.18
Update  : 2022.03.18
Source  : 10711.py
Purpose : bfs
url     : https://www.acmicpc.net/problem/10711
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
from collections import deque


def wave(empty_sands, visited, sands):
    global h, w

    ds = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

    time = 0

    while empty_sands:
        x, y = empty_sands.popleft()

        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx < h and 0 <= dy < w:
                if sands[dx][dy] != 0:
                    sands[dx][dy] -= 1
                    if sands[dx][dy] == 0:
                        visited[dx][dy] = visited[x][y] + 1
                        time = visited[dx][dy]
                        empty_sands.append((dx, dy))
    return time

if __name__ == "__main__":
    h, w = list(map(int, input().split()))
    sands = []
    empty_sands = deque()
    visited = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        temp = list(input())

        for j in range(w):
            if temp[j] == '.':
                empty_sands.append((i, j))
                temp[j] = 0
            else:
                temp[j] = int(temp[j])
        sands.append(temp)

    print(wave(empty_sands, visited, sands))