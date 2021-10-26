# # 연구소
#
# from itertools import combinations
#
# def dfs(array, x, y):
#     global n, m
#
#     ds = ((0, 1), (1, 0), (0, -1), (-1, 0))
#
#     for d in ds:
#         dx = x + d[0]
#         dy = y + d[1]
#
#         if 0 <= dx < n and 0 <= dy < m:
#             if array[dx][dy] == 0:
#                 array[dx][dy] = 2
#                 dfs(array, dx, dy)
#
#
# global n, m
#
# n, m = list(map(int, input().split()))
#
# array = []
# empty_zone = []
# wall_zone = []
# virus_zone = []
#
# for i in range(n):
#     temp = list(map(int, input().split()))
#
#     array.append(temp)
#
#     for j in range(m):
#         if temp[j] == 0:
#             empty_zone.append([i, j])
#         elif temp[j] == 1:
#             wall_zone.append([i, j])
#         elif temp[j] == 2:
#             virus_zone.append([i, j])
#
# combination_empty = combinations(empty_zone, 3)
# answer = 0
#
# for emptys in combination_empty:
#     temp_array = [i[:] for i in array]
#
#     for empty in emptys:
#         x, y = empty
#
#         temp_array[x][y] = 1
#
#     for i in range(n):
#         for j in range(m):
#             if temp_array[i][j] == 2:
#                 dfs(temp_array, i, j)
#
#     count = 0
#
#     for i in range(n):
#         for j in range(m):
#             if temp_array[i][j] == 0:
#                 count += 1
#
#     answer = max(count, answer)
#
# print(answer)

# 경쟁적 전염

from collections import deque

n, k = list(map(int, input().split()))

array = []
temp_q = []

for i in range(n):
    temp = list(map(int, input().split()))

    array.append(temp)

    for j in range(n):
        if temp[j] != 0:
            temp_q.append((i, j, temp[j], 0))

temp_q.sort(key=lambda x:x[2])
q = deque(temp_q)

s, x, y = list(map(int, input().split()))

ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

while q:
    v_x, v_y, v, v_s = q.popleft()

    if v_s == s:
        break

    for d in ds:
        dx = v_x + d[0]
        dy = v_y + d[1]

        if 0 <= dx < n and 0 <= dy < n:
            if array[dx][dy] == 0:
                array[dx][dy] = v
                q.append([dx, dy, v, v_s+1])

print(array[x-1][y-1])