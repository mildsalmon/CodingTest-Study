"""
Date    : 2022.03.14
Update  : 2022.03.14
Source  : 2251.py
Purpose : bfs
url     : https://www.acmicpc.net/problem/2251
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
from collections import deque


def bfs(x: int, y: int, waters: list) -> None:
    global a, b, c

    def move(x: int, y: int) -> bool:
        global visited

        if visited[x][y]:
            return False
        visited[x][y] = True
        return True

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        z = c - x - y

        if x == 0:
            waters.append(z)

        water = min(x, b - y)
        if move(x - water, y + water):
            q.append((x - water, y + water))

        water = min(x, c - z)
        if move(x - water, y):
            q.append((x - water, y))

        water = min(y, a - x)
        if move(x + water, y - water):
            q.append((x + water, y - water))

        water = min(y, c - z)
        if move(x, y - water):
            q.append((x, y - water))

        water = min(z, a - x)
        if move(x + water, y):
            q.append((x + water, y))

        water = min(z, b - y)
        if move(x, y + water):
            q.append((x, y + water))


if __name__ == "__main__":
    a, b, c = list(map(int, input().split()))

    waters = []
    visited = [[False for _ in range(b + 1)] for _ in range(a + 1)]
    visited[0][0] = True

    bfs(0, 0, waters)

    waters.sort()

    print(*waters, sep=' ')