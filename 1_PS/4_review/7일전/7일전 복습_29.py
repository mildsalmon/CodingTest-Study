# # 연구소
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
# def simulation(count, array, max_safe_zone):
#     global n, m
#
#     # 벽 3개 세웠을 때
#     if count == 3:
#         virus_array = [i[:] for i in array]
#         safe_zone = 0
#         # 바이러스 확산 시작
#         for i in range(n):
#             for j in range(m):
#                 if array[i][j] == 2:
#                     dfs(virus_array, i, j)
#         # safe zone 탐색
#         for i in range(n):
#             for j in range(m):
#                 if virus_array[i][j] == 0:
#                     safe_zone += 1
#
#         max_safe_zone = max(max_safe_zone, safe_zone)
#     # 벽 3개 세우지 못했을 때
#     else:
#         for i in range(n):
#             for j in range(m):
#                 if array[i][j] == 0:
#                     array[i][j] = 1
#                     count += 1
#
#                     max_safe_zone = simulation(count, array, max_safe_zone)
#
#                     count -= 1
#                     array[i][j] = 0
#
#     return max_safe_zone
#
# global n, m
#
# n, m = list(map(int, input().split()))
#
# array = []
# wall_array = []
# virus_array = []
#
# for i in range(n):
#     temp = list(map(int, input().split()))
#     array.append(temp)
#
#     for j in range(m):
#         if temp[j] == 1:
#             wall_array.append((i, j))
#
#         if temp[j] == 2:
#             virus_array.append((i, j))
#
# print(simulation(0, array, 0))

# 경쟁적 전염

from collections import deque

n, k = list(map(int, input().split()))

array = []
virus = []
virus_pos = []
virus_kind = []

for i in range(n):
    temp = list(map(int, input().split()))
    array.append(temp)

    for j in range(n):
        if temp[j] != 0:
            # 시간, x, y, 바이러스 종류
            virus.append((0, i, j, temp[j]))
            virus_pos.append((i, j))
            virus_kind.append(temp[j])

virus.sort(key=lambda x: x[3])
q = deque(virus)

s, x, y = list(map(int, input().split()))
x -= 1
y -= 1

ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

while q:
    v_s, v_x, v_y, v_t = q.popleft()

    if v_s == s:
        break

    for d in ds:
        dx = v_x + d[0]
        dy = v_y + d[1]

        if 0 <= dx < n and 0 <= dy < n:
            if (dx, dy) not in virus_pos:
                virus_pos.append((dx, dy))
                virus_kind.append(v_t)
                q.append((v_s+1, dx, dy, v_t))

if (x, y) in virus_pos:
    i = virus_pos.index((x, y))
    print(virus_kind[i])
else:
    print(0)