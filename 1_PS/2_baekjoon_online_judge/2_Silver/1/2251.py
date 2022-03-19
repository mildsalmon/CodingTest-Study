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


def water_move(water_amount: set):
    global a, b, c

    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        z = c - (x + y)

        if z in water_amount:
            continue

        if x == 0 and z > 0:
            water_amount.add(z)

        # x -> y
        temp_y = min(x, b)
        q.append((x - temp_y, temp_y))

        # x -> z
        temp_z = min(x, c)
        q.append((x - temp_z, y))

        # y -> x
        temp_x = min(y, a)
        q.append((temp_x, y - temp_x))

        # y -> z
        temp_z = min(y, c)
        q.append((x, y - temp_z))

        # z -> x
        temp_x = min(z, a)
        q.append((temp_x, y))

        # z -> y
        temp_y = min(z, b)
        q.append((x, temp_y))


if __name__ == "__main__":
    a, b, c = list(map(int, input().split()))

    water_amount = set()
    water_move(water_amount)

    answer = sorted(water_amount)
    print(*answer)