"""
Date    : 2021.12.23
Update  : 2022.02.28
Source  : 21922.py
Purpose : 구현 문제
url     : https://www.acmicpc.net/problem/21922
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys

input = sys.stdin.readline


def move(x, y, dn, positions):
    global airs, graph, n, m, ds

    if 0 <= x < n and 0 <= y < m:
        positions[x][y] = True

        if graph[x][y] == 0:
            dx = x + ds[dn][0]
            dy = y + ds[dn][1]

            move(dx, dy, dn, positions)
        elif graph[x][y] == 9:
            return
        else:
            new_dn = change_d(dn, graph[x][y])

            if new_dn == 99:
                return
            else:
                dx = x + ds[new_dn][0]
                dy = y + ds[new_dn][1]

                move(dx, dy, new_dn, positions)



def change_d(n, item):
    items = {1: [99, 1, 99, 3],
             2: [0, 99, 2, 99],
             3: [3, 2, 1, 0],
             4: [1, 0, 3, 2]}

    return items[item][n]


def count(positions):
    global n

    cnt = 0

    for i in range(n):
        cnt += positions[i].count(True)

    return cnt


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    graph = []
    positions = [[False]*m for _ in range(n)]
    airs = []
    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

    for i in range(n):
        temp = list(map(int, input().split()))

        for j in range(m):
            if temp[j] == 9:
                airs.append((i, j))
                positions[i][j] = True
        graph.append(temp)

    for x, y in airs:
        for dn in range(4):
            dx = x + ds[dn][0]
            dy = y + ds[dn][1]

            move(dx, dy, dn, positions)


    cnt = count(positions)

    print(cnt)