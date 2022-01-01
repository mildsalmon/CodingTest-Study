"""
Date    : 2022.01.01
Update  : 2022.01.01
Source  : 1261.py
Purpose : 다익스트라 / bfs
url     : https://www.acmicpc.net/problem/1261
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def bfs(start, graph) -> int:
    from collections import deque

    global n, m, ds

    q: deque = deque()
    q.append((start[0], start[1]))

    visited: list[[bool]] = [[False] * n for _ in range(m)]
    visited[start[0]][start[1]] = True

    while q:
        x, y = q.popleft()

        for d in ds:
            dx: int = x + d[0]
            dy: int = y + d[1]

            if x == m - 1 and y == n - 1:
                return graph[x][y]

            if 0 <= dx < m and 0 <= dy < n:
                if not visited[dx][dy]:
                    visited[dx][dy] = True
                    if graph[dx][dy] == 0:
                        graph[dx][dy] = graph[x][y]
                        q.appendleft((dx, dy))
                    elif graph[dx][dy] == 1:
                        graph[dx][dy] += graph[x][y]
                        q.append((dx, dy))

def dijkstra(start, graph) -> int:
    import heapq

    global n, m, ds

    q: list = []
    heapq.heappush(q, (graph[start[0]][start[1]], start[0], start[1]))

    visited: list[[bool]] = [[False] * n for _ in range(m)]
    visited[start[0]][start[1]] = True

    while q:
        cost, x, y = heapq.heappop(q)

        if x == m-1 and y == n-1:
            return cost

        for d in ds:
            dx: int = x + d[0]
            dy: int = y + d[1]

            if 0 <= dx < m and 0 <= dy < n:
                if not visited[dx][dy]:
                    visited[dx][dy] = True
                    if graph[dx][dy] == 0:
                        heapq.heappush(q, (cost, dx, dy))
                    elif graph[dx][dy] == 1:
                        heapq.heappush(q, (cost + 1, dx, dy))


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    graph = []

    ds = ((0, 1), (0, -1), (1, 0), (-1, 0))

    for _ in range(m):
        graph.append(list(map(int, input())))

    print(bfs((0,0), graph))