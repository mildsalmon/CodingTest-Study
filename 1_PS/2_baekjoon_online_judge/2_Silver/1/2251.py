"""
Date    : 2022.03.14
Update  : 2022.03.19
Source  : 2251.py
Purpose : bfs
url     : https://www.acmicpc.net/problem/2251
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
from collections import deque


def water_move(water_amount: set, visited: list):
    global a, b, c

    def check(x, y) -> bool:
        if visited[x][y]:
            return False
        visited[x][y] = True
        return True

    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        z = c - (x + y)

        if x == 0 and z >= 0:
            water_amount.add(z)

        # x -> y
        temp_y = min(x, b-y)
        if check(x-temp_y, y+temp_y):
            q.append((x-temp_y, y+temp_y))

        # x -> z
        temp_z = min(x, c-z)
        if check(x-temp_z, y):
            q.append((x-temp_z, y))

        # y -> x
        temp_x = min(y, a-x)
        if check(temp_x+x, y-temp_x):
            q.append((temp_x+x, y-temp_x))

        # y -> z
        temp_z = min(y, c-z)
        if check(x, y-temp_z):
            q.append((x, y-temp_z))

        # z -> x
        temp_x = min(z, a-x)
        if check(temp_x+x, y):
            q.append((temp_x+x, y))

        # z -> y
        temp_y = min(z, b-y)
        if check(x, temp_y+y):
            q.append((x, temp_y+y))


if __name__ == "__main__":
    a, b, c = list(map(int, input().split()))

    visited = [[False for _ in range(b+1)] for _ in range(a+1)]
    water_amount = set()

    water_move(water_amount, visited)

    answer = sorted(water_amount)
    print(*answer, sep=' ')