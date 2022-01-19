"""
Date    : 2021.11.25
Update  : 2021.11.25
Source  : Q39_화성탐사.py
Purpose :
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
# from collections import deque
#
# def dfs(i, j):
#
#     ds = ((0, 1), (0, -1), (1, 0), (-1, 0))
#
#     for d in ds:
#         dx = i + d[0]
#         dy = j + d[1]
#
#         if 0 <= dx < n and 0 <= dy < n:
#             temp_graph[dx][dy] = min(temp_graph[dx][dy], temp_graph[i][j] + graph[dx][dy])
#             dfs(dx, dy)
#
# for t in range(int(input())):
#     # 탐사 공간
#     n = int(input())
#     graph = []
#
#     for i in range(n):
#         temp = list(map(int, input().split()))
#         graph.append(temp)
#
#     temp_graph = [[1e9] * n for _ in range(n)]
#
#
#     for i in range(n):
#         for j in range(n):
#             dfs(i, j)
#
#
#     q = deque()
#     q.append((0, 0))
#
#
#     while q:
#         x, y = q.popleft()
#
#         for d in ds:
#             dx = x + d[0]
#             dy = y + d[1]
#
#             if 0 <= dx < n and 0 <= dy < n:
#                 if temp_graph[dx][dy] == 1e9:
#                     q.append((dx, dy))
#                 temp_graph[dx][dy] = min(temp_graph[dx][dy], temp_graph[x][y] + graph[dx][dy])
#
#     print(*temp_graph, sep='\n')
#     print(temp_graph[n-1][n-1])
#
#     # for k in range(n):
#     #     for i in range(n):
#     #         for j in range(n):
#     #             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#     #
#     # print(graph[n-1][n-1])

import heapq

for t in range(int(input())):
    # 탐사 공간
    n = int(input())
    # 탐사 공간에 대한 비용
    graph = []

    for i in range(n):
        graph.append(list(map(int, input().split())))
    # 다익스트라를 위한 q
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    # 상하좌우 탐색을 위한 ds
    ds = ((0, 1), (0, -1), (1, 0), (-1, 0))

    distance = [[1e9] * n for _ in range(n)]
    distance[0][0] = graph[0][0]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx and dx < n and 0 <= dy and dy < n:
                cost = dist + graph[dx][dy]

                if cost < distance[dx][dy]:
                    distance[dx][dy] = cost
                    heapq.heappush(q, (cost, dx, dy))

    print(distance[n-1][n-1])

# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4