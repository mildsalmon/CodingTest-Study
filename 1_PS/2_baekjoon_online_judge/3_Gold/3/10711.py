"""
Date    : 2022.03.18
Update  : 2022.03.20
Source  : 10711.py
Purpose : bfs
url     : https://www.acmicpc.net/problem/10711
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
from collections import deque


def wave(sea):
    global beach, h, w

    ds = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

    visited = [[0 for _ in range(w)] for _ in range(h)]
    cnt = 0

    while sea:
        x, y = sea.popleft()

        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx < h and 0 <= dy < w:
                if beach[dx][dy] != 0:
                    beach[dx][dy] -= 1
                    if beach[dx][dy] == 0:
                        visited[dx][dy] = max(visited[dx][dy], visited[x][y]+1)
                        cnt = max(visited[dx][dy], cnt)
                        sea.append((dx, dy))

    # print(*visited, sep='\n')
    # print(*beach, sep='\n')
    return cnt


if __name__ == "__main__":
    h, w = list(map(int, input().split()))
    beach = []
    sea = deque()

    for i in range(h):
        temp = list(input())

        for j in range(w):
            if temp[j] == '.':
                sea.append((i, j))
                temp[j] = 0
            else:
                temp[j] = int(temp[j])
        beach.append(temp)

    print(wave(sea))
    # print(*beach, sep='\n')
