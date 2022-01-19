# # 왕실의 나이트
#
# s = input()
#
# y = ord(s[0]) - ord('a') + 1
# x = int(s[1])
#
# move = [(-2, 1), (-2, 1),
#         (-1, 2), (1, 2),
#         (2, 1), (-2, -1),
#         (-1, -2), (1, -2)]
# count = 0
#
# for m in move:
#     dx = x + m[0]
#     dy = y + m[1]
#
#     if 0 < dx <= 8 and 0 < dy <= 8:
#         count += 1
#
# print(count)
#

# 게임 개발

def dfs(graph, x, y):
    global n, m, count

    ds = ((-1, 0), (0, 1), (1, 0), (0, -1))

    for d in ds:
        dx = x + d[0]
        dy = y + d[1]

        if 0 <= dx < n and 0 <= dy < m:
            if graph[dx][dy] == 0:
                graph[dx][dy] = 2
                count += 1
                dfs(graph, dx, dy)
            else:
                dx = dx-d[0]
                dy = dy-d[1]

                if graph[dx][dy] == 0:
                    dfs(graph, dx, dy)
                else:
                    continue

global n, m, count

n, m = list(map(int, input().split()))
A, B, D = list(map(int, input().split()))


graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

graph[A][B] = 2
count = 1

dfs(graph, A, B)

print(count)