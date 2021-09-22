# def dfs(graph, x, y):
#     d = ((-1, 0), (1, 0), (0, -1), (0, 1))
#
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return None
#     if graph[x][y] == 1:
#         return None
#     if graph[x][y] == 0:
#         graph[x][y] = 2
#
#         dfs(graph, x - 1, y)
#         dfs(graph, x + 1, y)
#         dfs(graph, x, y + 1)
#         dfs(graph, x, y - 1)
#
#         # if graph[x][y] != 2:
#         #     dfs(graph, x - 1, y)
#         #     dfs(graph, x + 1, y)
#         #     dfs(graph, x, y - 1)
#         #     dfs(graph, x, y + 1)
#         return True
#
# global n
# global m ###
# # 세로, 가로
# n, m = list(map(int, input().split()))
# # 0 빈칸 / 1 벽 / 2 바이러스
# graph = []
#
# for i in range(n):
#     temp = list(map(int, input().split()))
#
#     graph.append(temp)
#
#
# graph_check = [i[:] for i in graph]
#
# answer = 0
# end_count = (m*n)
#
# while end_count > 0:
#     wall_count = 3
#     graph_temp = [i[:] for i in graph]
#     safe_count = 0
#
#     for i in range(n):
#         for j in range(m):
#             if graph_temp[i][j] == 0 and graph_check[i][j] == 0:
#                 graph_temp[i][j] = 1
#                 wall_count -= 1
#
#             if wall_count == 0:
#                 break
#         graph_check[i][j-2] = 1
#         if wall_count == 0:
#             break
#
#     for i in range(n):
#         for j in range(m):
#             if graph_temp[i][j] == 2:
#                 graph_temp[i][j] = 0
#                 dfs(graph_temp, i, j)
#
#     for i in range(n):
#         for j in range(m):
#             if graph_temp[i][j] == 0:
#                 safe_count += 1
#
#     answer = max(answer, safe_count)
#     end_count -= 1
#
#     print(*graph_temp, sep='\n')
#     print()
#     print(*graph_check, sep='\n')
#     print()
#
# print(answer)
#

def check_virus(graph, x, y):
    global n, m

    ds = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for d in ds:
        dx = x + d[0]
        dy = y + d[1]

        if dx < 0 or dx >= n or dy < 0 or dy >= m:
            continue
        if graph[dx][dy] == 1:
            continue

        if graph[dx][dy] != 2:
            graph[dx][dy] = 2
            check_virus(graph, dx, dy)


def dfs(count, graph):
    global answer

    if count == 3:
        # 벽 3개 다 침
        temp_graph = [i[:] for i in graph]

        for i in range(n):
            for j in range(m):
                if graph[i][j] == 2:
                    check_virus(temp_graph, i, j)
        safe_count = 0
        for i in range(n):
            for j in range(m):
                if temp_graph[i][j] == 0:
                    safe_count += 1
        answer = max(answer, safe_count)
        # return answer
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    count += 1
                    graph[i][j] = 1
                    dfs(count, graph)
                    graph[i][j] = 0
                    count -= 1


global n, m
n, m = list(map(int, input().split()))

graph = []
global answer
answer = 0
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

bfs(0, graph)

print(answer)