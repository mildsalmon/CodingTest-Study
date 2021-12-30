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
                temp.append((-dx*n+dy, dx, dy))
        distance[i].append(temp)

visited = [[False] * m for _ in range(n)]

q = []
heapq.heappush(q, (graph[0][0], 0, 0, 0))

break_wall_count = 0

while q:
    wall, num, y, x = heapq.heappop(q)

    if not visited[x][y]:
        if x == n-1 and y == m-1:
            break

        visited[x][y] = True
        print(x, y)
        if wall == 1:
            break_wall_count += 1
            graph[x][y] = 0

        for nnum, nx, ny in distance[x][y]:
            if not visited[nx][ny]:
                heapq.heappush(q, (graph[nx][ny], nnum, ny, nx))

        print(*graph, sep='\n')
        print()
        print(*visited, sep='\n')
        print()
        print(break_wall_count)

print(break_wall_count)
