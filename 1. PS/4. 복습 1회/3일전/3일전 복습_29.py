# 연구소

# from itertools import combinations
#
# def dfs(graph, x, y):
#     global n, m
#
#     ds = ((1, 0), (-1, 0), (0, -1), (0, 1))
#
#     for d in ds:
#         dx = x + d[0]
#         dy = y + d[1]
#
#         if 0 <= dx < n and 0 <= dy < m:
#             if graph[dx][dy] == 0:
#                 graph[dx][dy] = 2
#                 dfs(graph, dx, dy)
#             else:
#                 continue
#         else:
#             continue
#
# global n, m
#
# n, m = list(map(int, input().split()))
#
# graph = []
# empty = []
# virus = []
#
# for i in range(n):
#     temp = list(map(int, input().split()))
#
#     graph.append(temp)
#
#     for j in range(len(temp)):
#         if temp[j] == 0:
#             empty.append((i, j))
#         elif temp[j] == 2:
#             virus.append((i, j))
#
# empty_combinations = list(combinations(empty, 3))
# answer = 0
#
# for emptys in empty_combinations:
#     # 벽 세우기
#     for empty in emptys:
#         x, y = empty
#         graph[x][y] = 1
#
#     # 바이러스 확산
#     temp_graph = [i[:] for i in graph]
#
#     for v in virus:
#         vx, vy = v
#         dfs(temp_graph, vx, vy)
#
#     count = 0
#     for i in range(n):
#         for j in range(m):
#             if temp_graph[i][j] == 0:
#                 count += 1
#     answer = max(count, answer)
#
#     # print(*temp_graph, sep='\n')
#     # print()
#
#     # 벽 내리기
#     for empty in emptys:
#         x, y = empty
#         graph[x][y] = 0
#
# print(answer)

# 28분 / pass

# 경쟁적 전염

from collections import deque

n, k = list(map(int, input().split()))

graph = []
virus = []

for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

    for j in range(len(temp)):
        if temp[j] != 0:
            virus.append([temp[j], 0, i, j])

s, x, y = list(map(int, input().split()))

virus.sort()
q = deque(virus)

# time = 0

ds = ((1, 0), (-1, 0), (0, 1), (0, -1))

while q:
    # print(q)
    virus_num, v_time, v_x, v_y = q.popleft()
    if v_time == s:
        break
    for d in ds:
        dx = v_x + d[0]
        dy = v_y + d[1]

        if 0 <= dx < n and 0 <= dy < n:
            if graph[dx][dy] == 0:
                graph[dx][dy] = virus_num
                q.append([virus_num, v_time+1, dx, dy])
    # print(*graph, sep='\n')
    # print()
    # time += 1

print(graph[x-1][y-1])