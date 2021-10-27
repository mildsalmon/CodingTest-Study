# # 미래도시
#
# # A - K - X
#
# n, m = list(map(int, input().split()))
# array = [[1e9] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             array[i][j] = 0
#
# for i in range(m):
#     x, y = list(map(int, input().split()))
#
#     array[x-1][y-1] = 1
#     array[y-1][x-1] = 1
#
# x, k = list(map(int, input().split()))
#
# for a in range(n):
#     for i in range(n):
#         for j in range(n):
#             array[i][j] = min(array[i][j], array[i][a] + array[a][j])
#
#
# answer = array[0][k-1] + array[k-1][x-1]
#
# if answer >= 1e9:
#     print(-1)
# else:
#     print(answer)

# 전보

import heapq

n, m, c = list(map(int, input().split()))

array = [[] for i in range(n+1)]
distance = [1e9] * (n+1)

# distance[c-1] = 0

for i in range(m):
    x, y, z = list(map(int, input().split()))

    array[x].append((z, y))

q = []
heapq.heappush(q, (0, c))

count = 0
answer = 0

while q:
    now_time, now_node = heapq.heappop(q)

    if distance[now_node] >= now_time:

        for i in array[now_node]:
            next_time, next_node = i

            total_time = now_time + next_time

            if total_time < distance[next_node]:
                distance[next_node] = total_time
                heapq.heappush(q, (total_time, next_node))
                count += 1
                answer = max(total_time, answer)

print(count, answer)