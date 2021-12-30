"""
Date    : 2021.12.30
Update  : 2021.12.30
Source  : 1261.py
Purpose : 다익스트라 / BFS
url     : https://www.acmicpc.net/problem/1261
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import heapq

m, n = list(map(int, input().split()))
graph = []

for i in range(n):
    temp = list(map(int, input()))
    graph.append(temp)

ds = ((1,0), (0, 1), (-1, 0), (0, -1))

visited = [[False] * m for _ in range(n)]

q = []
heapq.heappush(q, (graph[0][0], 0, 0))

break_wall_count = 0

while q:
    wall, x, y = heapq.heappop(q)

    if not visited[x][y]:
        if x == n-1 and y == m-1:
            break_wall_count = wall
            break

        visited[x][y] = True
        # 상,하,좌,우 4방향 탐색
        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx < n and 0 <= dy < m:
                if not visited[dx][dy]:
                    if graph[dx][dy] == 1:
                        heapq.heappush(q, (wall + 1, dx, dy))
                    else:
                        heapq.heappush(q, (wall, dx, dy))

print(break_wall_count)
