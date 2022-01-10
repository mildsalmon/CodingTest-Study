"""
Date    : 2022.01.10
Update  : 2022.01.10
Source  : 1520.py
Purpose : 재귀
url     : https://www.acmicpc.net/problem/1520
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
def dfs(x, y, visited):
    global n, m, graph

    ds = ((0, -1), (0, 1), (-1, 0), (1, 0))

    if x == m-1 and y == n-1:
        return 1

    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0

    for d in ds:
        dx = x + d[0]
        dy = y + d[1]

        if 0 <= dx < m and 0 <= dy < n:
            if graph[dx][dy] < graph[x][y]:
                visited[x][y] += dfs(dx, dy, visited)

    return visited[x][y]

if __name__ == "__main__":
    m, n = list(map(int, input().split()))
    graph = []

    for i in range(m):
        temp = list(map(int, input().split()))
        graph.append(temp)

    visited = [[-1]*n for _ in range(m)]

    dfs(0, 0, visited)

    print(visited[0][0])