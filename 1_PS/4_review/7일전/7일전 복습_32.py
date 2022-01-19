# 인구이동

from collections import deque

n, l, r = list(map(int, input().split()))
array = []

for i in range(n):
    array.append(list(map(int, input().split())))

time = 0
ds = ((1, 0), (0, 1), (-1, 0), (0, -1))

while True:
    temp = [[False] * n for i in range(n)]
    exit_count = 0

    for i in range(n):
        for j in range(n):
            if not temp[i][j]:
                q = deque()
                q.append((i, j))
                open_countrys = [(i, j)]
                sum_pop = array[i][j]
                pop_count = 1
                temp[i][j] = True

                while q:
                    x, y = q.popleft()

                    for d in ds:
                        dx = x + d[0]
                        dy = y + d[1]

                        if 0 <= dx < n and 0 <= dy < n:
                            if temp[dx][dy] == False:
                                diff = abs(array[x][y] - array[dx][dy])
                                if l <= diff <= r:
                                    temp[dx][dy] = True
                                    open_countrys.append((dx, dy))
                                    sum_pop += array[dx][dy]
                                    pop_count += 1
                                    q.append((dx, dy))

                population = (sum_pop // pop_count)

                for open_country in open_countrys:
                    x, y = open_country
                    array[x][y] = population

            elif temp[i][j]:
                exit_count += 1

    if exit_count == 0:
        break
    else:
        time += 1

print(time)

# from collections import deque
#
# n, l, r = list(map(int, input().split()))
# array = []
#
# for i in range(n):
#     array.append(list(map(int, input().split())))
#
# time = 0
# ds = ((1, 0), (0, 1), (-1, 0), (0, -1))
#
# while True:
#     temp = [[False] * n for i in range(n)]
#     exit_count = 0
#
#     for i in range(n):
#         for j in range(n):
#             if not temp[i][j]:
#                 q = deque()
#                 q.append((i, j))
#                 open_countrys = []
#                 sum_pop = 0
#                 pop_count = 0
#
#                 while q:
#                     x, y = q.popleft()
#                     temp[x][y] = True
#                   # q 안에 있는 값은 중복처리가 되지 않음.
#                   # 따라서, open_countrys, sum_pop, pop_count에는 중복된 좌표가 들어갈 수밖에 없음.
#                     open_countrys.append((x, y))
#                     sum_pop += array[x][y]
#                     pop_count += 1
#
#                     for d in ds:
#                         dx = x + d[0]
#                         dy = y + d[1]
#
#                         if 0 <= dx < n and 0 <= dy < n:
#                             if temp[dx][dy] == False:
#                                 diff = abs(array[x][y] - array[dx][dy])
#                                 if l <= diff <= r:
#                                     q.append((dx, dy))
#
#                 population = (sum_pop // pop_count)
#
#                 for open_country in open_countrys:
#                     x, y = open_country
#                     array[x][y] = population
#
#             elif temp[i][j]:
#                 exit_count += 1
#
#     if exit_count == 0:
#         break
#     else:
#         time += 1
#
# print(time)