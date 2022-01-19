# #-*- coding: utf-8 -*-
#
# def dfs(graph, s, x, y):
#     global n
#
#     ds = ((-1, 0), (1, 0), (0, -1), (0, 1))
#
#     # for i in range(s):
#     if s < 0:
#         return
#     else:
#         s -= 1
#         for d in ds:
#             dx = x + d[0]
#             dy = y + d[1]
#
#             if dx < 0 or dx >= n or dy < 0 or dy >= n:
#                 continue
#             if graph[dx][dy] == 0 and temp_graph[dx][dy] == 0:
#                 graph[dx][dy] = graph[x][y]
#             elif graph[dx][dy] != 0 and temp_graph[dx][dy] == 0:
#                 graph[dx][dy] = min(graph[x][y], graph[dx][dy])
#                 continue
#             elif graph[dx][dy] != 0 and temp_graph[dx][dy] != 0:
#                 continue
#                 # graph[dx][dy] = max(graph[dx][dy], temp_graph[x][y])
#             dfs(graph, s, dx, dy)
#
# global n
#
# n, k = list(map(int, input().split()))
#
# graph = []
# # 0, 0부터 리스트에 담는거 까먹음
# for i in range(n):
#     temp = list(map(int, input().split()))
#     graph.append(temp)
#
# s, x, y = list(map(int, input().split()))
# x -= 1
# y -= 1
# temp_graph = [i[:] for i in graph]
#
# # for i in range(n):
# #     for j in range(n):
# #         dfs(graph, s, i, j)
# #
# for i in range(s):
#     for i in range(n):
#         for j in range(n):
#             if temp_graph[i][j] != 0:
#                 dfs(graph, s, i, j)
#
# if graph[x][y] == 0:
#     print(0)
# else:
#     print(graph[x][y])
#
# print(*graph, sep='\n')
#
# # 반례
#
# # 4 2
# # 1 0 0 0
# # 0 0 0 0
# # 0 0 0 0
# # 0 0 0 2
# # 3 3 2
from collections import deque

n, k = list(map(int, input().split()))

graph = [[0] * (n+1) for i in range(n+1)]
data = []

for i in range(1, n+1):
    temp = list(map(int, input().split()))

    for j in range(1, n+1):
        graph[i][j] = temp[j-1]

        if graph[i][j] != 0:
            data.append([graph[i][j], 0, i, j])

# for i in range(1, n+1):
#     temp = [0]
#     temp.append(list(map(int, input().split())))
#     # graph.append(temp)
#     for t in range(len(temp)):
#         if temp[t] != 0:
#             data.append([temp[t], 0, i, t])

s, x, y = list(map(int, input().split()))

data.sort()
q = deque(data)

ds = ((-1, 0), (1, 0), (0, -1), (0, 1))

while q:
    q_value, q_s, q_x, q_y = q.popleft()

    if q_s == s:
        break

    for d in ds:
        dx = q_x + d[0]
        dy = q_y + d[1]

        if dx < 1 or dx > n or dy < 1 or dy > n:
            continue

        if graph[dx][dy] != 0:
            continue

        graph[dx][dy] = q_value
        q.append([q_value, q_s+1, dx, dy])

print(graph[x][y])

# print(*graph, sep='\n')