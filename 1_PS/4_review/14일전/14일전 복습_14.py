# # Ch9_최단 경로_미래 도시
#
# # A -> K -> X
# # 양방향 / 시간 1
#
# import heapq
#
# def dijkstra(graph, start, end):
#     distance = [1e9] * (n + 1)
#     distance[start] = 0
#
#     q = []
#     heapq.heappush(q, [0, start])
#
#     while q:
#         now_cost, now_node = heapq.heappop(q)
#
#         if now_cost > distance[now_node]:
#             continue
#
#         for j in graph[now_node]:
#             next_node = j[0]
#             next_cost = j[1]
#
#             cost = now_cost + next_cost
#
#             if cost < distance[next_node]:
#                 distance[next_node] = cost
#                 heapq.heappush(q, [cost, next_node])
#
#     return distance[end]
#
# n, m = list(map(int, input().split()))
#
# graph = [[]*(n+1) for _ in range(n+1)]
#
# for i in range(1, m+1):
#     a, b = list(map(int, input().split()))
#
#     graph[a].append([b, 1])
#     graph[b].append([a, 1])
# # print(*graph, sep='\n')
# x, k = list(map(int, input().split()))
#
#
# answer = dijkstra(graph, 1, k) + dijkstra(graph, k, x)
#
# if answer >= 1e9:
#     print(-1)
# else:
#     print(answer)

# # Ch9_최단 경로_전보
#
# import heapq
#
# def dijkstra(start, distance, graph):
#     distance[start] = 0
#
#     q = []
#     heapq.heappush(q, (0, start))
#
#     while q:
#         now_cost, now_node = heapq.heappop(q)
#
#         if now_cost > distance[now_node]:
#             continue
#
#         for i in graph[now_node]:
#             next_node = i[0]
#             next_cost = i[1]
#
#             cost = next_cost + now_cost
#
#             if cost < distance[next_node]:
#                 distance[next_node] = cost
#                 heapq.heappush(q, (cost, next_node))
#
#
# n, m, c = list(map(int, input().split()))
#
# graph = [[] for _ in range(n+1)]
#
# for i in range(m):
#     x, y, z = list(map(int, input().split()))
#
#     graph[x].append([y, z])
#
# distance = [1e9] * (n+1)
#
# dijkstra(c, distance, graph)
# count = -1
# time = 0
# for i in range(len(distance)):
#     if distance[i] >= 1e9:
#         pass
#     else:
#         count += 1
#         time = max(time, distance[i])
# print(count, time)
#
# # 22분 21초

# Ch9_최단 경로_미래 도시

# 플로이드 와샬

n, m = list(map(int, input().split()))

graph = [[1e9]*(n+1) for _ in range(n+1)]

for i in range(1, m+1):
    a, b = list(map(int, input().split()))

    graph[a][b] = 1
    graph[b][a] = 1

x, k = list(map(int, input().split()))

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

for l in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][l] + graph[l][j])

answer = graph[1][k] + graph[k][x]

if answer >= 1e9:
    print(-1)
else:
    print(answer)

# 7분 7초초