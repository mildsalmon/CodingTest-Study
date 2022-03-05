"""
Date    : 2021.12.23
Update  : 2022.03.05
Source  : 21922.py
Purpose : 구현 문제
url     : https://www.acmicpc.net/problem/21922
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys

input = sys.stdin.readline


def wind_move(x, y, visited):
    global airs, n, m, graph

    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

    visited[x][y] = True

    for d in range(4):
        dx = x + ds[d][0]
        dy = y + ds[d][1]

        while 0 <= dx < n and 0 <= dy < m:
            visited[dx][dy] = True

            if graph[dx][dy] == 0:
                dx = dx + ds[d][0]
                dy = dy + ds[d][1]
            elif graph[dx][dy] == 9:
                break
            else:
                d = change_wind(d, graph[dx][dy])
                dx = dx + ds[d][0]
                dy = dy + ds[d][1]



def change_wind(d, item):
    items = {1: [2, 1, 0, 3],
             2: [0, 3, 2, 1],
             3: [3, 2, 1, 0],
             4: [1, 0, 3, 2]}

    return items[item][d]


def count_place(visited):
    count = 0

    for i in range(len(visited)):
        count += visited[i].count(True)

    return count


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    graph = []
    airs = []

    for i in range(n):
        temp = list(map(int, input().split()))

        for j in range(m):
            if temp[j] == 9:
                airs.append((i,j))
        graph.append(temp)

    visited = [[False] * m for _ in range(n)]

    for x, y in airs:
        wind_move(x, y, visited)

    print(count_place(visited))