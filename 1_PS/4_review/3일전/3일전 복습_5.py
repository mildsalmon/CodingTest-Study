# n, m = list(map(int, input().split()))
#
# array = []
# result = 0
#
# for i in range(n):
#     array.append(list(map(int, input())))
#
# def dfs(x, y):
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return 0
#     if array[x][y] == 0:
#         array[x][y] = 1
#
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         dfs(x-1, y)
#
#         return 1
#     else:
#         return 0
#
#
# for i in range(n):
#     for j in range(m):
#         result = result + dfs(i, j)
#
# print(result)

# ---------------------------------

# from collections import deque
#
# n, m = list(map(int, input().split()))
# game_map = []
#
# ds = [(0, -1), (1, 0), (0, 1), (-1, 0)]
#
# pos = deque()
# pos.append([0,0])
#
# for i in range(n):
#     game_map.append(list(map(int, input())))
#
# while pos:
#     x, y = pos.popleft()
#
#     for d in ds:
#         dx = x + d[0]
#         dy = y + d[1]
#
#         if dx <= -1 or dx >= n or dy <= -1 or dy >= m:
#             continue
#         if game_map[dx][dy] == 1:
#             game_map[dx][dy] = game_map[x][y] + 1
#             pos.append([dx, dy])
#         else:
#             continue
#
#     if game_map[n-1][m-1] != 1:
#         break
#
# print(game_map[n-1][m-1])