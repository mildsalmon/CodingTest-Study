# # BFS
# from collections import deque
# import sys
#
# # n, m, k, x = list(map(int, input().split()))
# n, m, k, x = list(map(int, input().split()))
#
# array = [[] for i in range(n+1)]
# count = [k+1] * (n+1)
#
# count[0] = 0
# count[x] = 0
#
# for _ in range(m):
#     a, b = list(map(int ,input().split()))
#     array[a].append(b)
#
# q = deque()
# q.append(x)
#
# while q:
#     src = q.popleft()
#
#     for i in array[src]:
#         if count[i] > count[src] + 1:
#             count[i] = count[src] + 1
#             q.append(i)
#
# if k not in count:
#     print(-1)
# else:
#     for i in range(len(count)):
#         if count[i] == k:
#             print(i)

# 다익스트라

import heapq
import sys

n, m, k, x = list(map(int, sys.stdin.readline().split()))

graph = [[] for i in range(n+1)]
distance = [1e9] * (n+1)

for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))

    graph[a].append((1, b))

q = []
heapq.heappush(q, (0, x))
distance[x] = 0

while q:
    cost, src = heapq.heappop(q)

    if cost > distance[src]:
        continue

    for i in graph[src]:
        dest_cost, dest_node = i

        total_cost = dest_cost + cost

        if total_cost < distance[dest_node]:
            distance[dest_node] = total_cost
            heapq.heappush(q, (distance[dest_node], dest_node))

if k not in distance:
    print(-1)
else:
    for i in range(len(distance)):
        if distance[i] == k:
            print(i)