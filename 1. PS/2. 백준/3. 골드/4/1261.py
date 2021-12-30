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

distance = [[] for _ in range(n)]

ds = ((1,0), (0, 1), (-1, 0), (0, -1))

for i in range(n):
    for j in range(m):
        temp = []

        for d in ds:
            dx = i + d[0]
            dy = j + d[1]

            if 0 <= dx < n and 0 <= dy < m:
                temp.append((dx, dy))
        distance[i].append(temp)

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

        for nx, ny in distance[x][y]:
            if not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    heapq.heappush(q, (wall + 1, nx, ny))
                else:
                    heapq.heappush(q, (wall, nx, ny))

print(break_wall_count)
