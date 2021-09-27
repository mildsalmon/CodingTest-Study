# from collections import deque
#
# N, L, R = list(map(int, input().split()))
#
# graph = []
# # diff_graph = [[0] * 4 for _ in range(N)]
# diff_graph = []
#
# for i in range(N):
#     graph.append(list(map(int, input().split())))
#
# ds = ((-1, 0), (0, 1), (1, 0), (0, -1))
#
# q = deque()
# # 좌표, 시간
# q.append([0, 0])
#
# while True:
#     time = 0
#     answer = [[0] * N for _ in range(N)]
#     while q:
#         x, y = q.popleft()
#
#         for d_i in range(len(ds)):
#             dx = x + ds[d_i][0]
#             dy = y + ds[d_i][1]
#
#             if 0 <= dx < N and 0 <= dy < N:
#                 value = abs(graph[x][y] - graph[dx][dy])
#                 if L <= value <= R:
#                     q.append([dx, dy])
#                     answer[dx][dy] += 1
#                 else:
#                     continue
#             else:
#                 continue
#     total_pop = 0
#     total_count = 0
#
#     for i in range(N):
#         for j in range(N):
#             if answer[i][j] > 0:
#                 total_pop += graph[i][j]
#                 total_count += 1
#
#     if total_count == 0:
#         break
#
#     for i in range(N):
#         for j in range(N):
#             if answer[i][j] > 0:
#                 graph[i][j] = (total_pop // total_count)
#
#     time += 1
#
# print(time)
#
# # print(diff_graph)
#
#     # for i in range(N):
#     #     for j in range(N):
#     #         diff_list = [0] * 4
#     #         for d_i in range(len(ds)):
#     #             dx = i + ds[d_i][0]
#     #             dy = j + ds[d_i][1]
#     #
#     #             if 0 <= dx < N and 0 <= dy < N:
#     #                 value = abs(graph[i][j] - graph[dx][dy])
#     #                 diff_list[d_i] = value
#     #             else:
#     #                 diff_list[d_i] = 0
#     #         diff_graph.append(diff_list)
#

# 50분 / 실패

from collections import deque

def bfs(x, y, check, graph):
    global N, group_num
    unit = [(x, y)]

    # 간 곳 카운트
    go_count = 1
    result = graph[x][y]
    check[x][y] = group_num
    q = deque()
    q.append([x,y])

    ds = ((-1, 0), (0, 1), (1, 0), (0, -1))

    while q:
        x, y = q.popleft()
        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx < N and 0 <= dy < N:
                if check[dx][dy] == -1:
                    diff = abs(graph[x][y] - graph[dx][dy])
                    if L <= diff <= R:
                        check[dx][dy] = group_num
                        q.append([dx, dy])
                        result += graph[dx][dy]
                        go_count += 1
                        # unit.append((dx, dy))
    for i in range(N):
        for j in range(N):
            if check[i][j] == group_num:
                graph[i][j] = result // go_count
            # 딱히 if go_count != 0: 해줄 필요 없음
    # for x, y in unit:
    #     graph[x][y] = result // go_count

    return go_count

global N, group_num

N, L, R = list(map(int, input().split()))

graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

# 매일이 지나가는 것
time = 0
while True:
    # 미 개척지 체크
    check = [[-1] * N for i in range(N)]
    group_num = 0

    for i in range(N):
        for j in range(N):
            if check[i][j] == -1:
                go_count = bfs(i, j, check, graph)
                group_num += 1

    if group_num == N*N:
    # if -1 in check:
    # if go_count == 0:
        break
    time += 1

print(time)
