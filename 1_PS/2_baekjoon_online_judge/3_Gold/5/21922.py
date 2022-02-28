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


def move(x, y, positions):
    global graph, n, m

    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

    for dn in range(4):
        dx = x + ds[dn][0]
        dy = y + ds[dn][1]

        while 0 <= dx < n and 0 <= dy < m:
            positions[dx][dy] = True

            if graph[dx][dy] == 0:
                dx = dx + ds[dn][0]
                dy = dy + ds[dn][1]
            elif graph[dx][dy] == 9:
                break
            else:
                dn = change_d(dn, graph[dx][dy])

                if dn == 99:
                    break
                else:
                    dx = dx + ds[dn][0]
                    dy = dy + ds[dn][1]


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

    for i in range(n):
        temp = list(map(int, input().split()))

        for j in range(m):
            if temp[j] == 9:
                airs.append((i, j))
                positions[i][j] = True
        graph.append(temp)

    for x, y in airs:
        move(x, y, positions)


    cnt = count(positions)

    print(cnt)