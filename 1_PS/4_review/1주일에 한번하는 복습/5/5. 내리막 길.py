"""
Date    : 2022.01.15
Update  : 2022.01.15
Source  : 1520.py
Purpose :
url     : https://www.acmicpc.net/problem/1520
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys

sys.setrecursionlimit(10000)

def dfs(x: int, y: int, visited: list) -> int:
    global m, n, graph

    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

    if x == m-1 and y == n-1:
        return 1

    visited[x][y] = 0

    for d in ds:
        dx = x + d[0]
        dy = y + d[1]

        if 0 <= dx < m and 0 <= dy < n:
            if graph[dx][dy] < graph[x][y]:
                if visited[dx][dy] != -1:
                    visited[x][y] += visited[dx][dy]
                    continue
                else:
                    visited[x][y] += dfs(dx, dy, visited)

    return visited[x][y]

if __name__ == "__main__":
    m, n = list(map(int, input().split()))

    graph = []

    for _ in range(m):
        temp = list(map(int, input().split()))

        graph.append(temp)

    visited = [[-1] * n for _ in range(m)]

    print(dfs(0, 0, visited))