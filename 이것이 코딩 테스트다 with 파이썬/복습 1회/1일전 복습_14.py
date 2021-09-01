# # Ch9_최단경로_미래도시
#
# INF = 1e9
# n, m = list(map(int, input().split()))
#
# graph = [[INF] * (n+1) for _ in range(n+1)]
#
# for _ in range(m):
#     a, b = list(map(int, input().split()))
#     graph[a][b] = 1
#     graph[b][a] = 1
#
# x, k = list(map(int, input().split()))
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j:
#             graph[i][j] = 0
#
# for z in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             if graph[a][b] > graph[a][z] + graph[z][b]:
#                 graph[a][b] = graph[a][z] + graph[z][b]
#
# result = graph[1][k] + graph[k][x]
#
# if result >= INF:
#     print(-1)
# else:
#     print(result)
#

# CH9_최단경로_전보

import heapq

INF = int(1e9)

n, m, c = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    x, y, z = list(map(int, input().split()))
    graph[x].append((y, z))

q = []
heapq.heappush(q, (0, c))
distance[c] = 0

while q:
    dist, node = heapq.heappop(q)

    if distance[node] < dist:
        continue

    for i in graph[node]:
        cost = i[1] + dist

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

count = 0
result_time = 0

for i in distance:
    if i >= INF:
        pass
    else:
        count = count + 1
        result_time = max(i, result_time)

print(count-1, result_time)

# 아직도 다익스트라가 완벽하지는 않은듯