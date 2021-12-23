"""
Date    : 2021.12.23
Update  : 2021.12.23
Source  : 21922.py
Purpose :
url     : https://www.acmicpc.net/problem/5567
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def dfs(graph, visited, x, y, d):
    global n, m

    if 0 <= x < n and 0 <= y < m:
        if d[0] == 0 and d[1] == 0:
            pass
        else:
            if graph[x][y] != 9:
                visited[x][y] = True
                dd = d[:]

                if graph[x][y] == 1:
                    if dd[1] == 1 or dd[1] == -1:
                        dd = (0, 0)
                    elif dd[0] == 1 or dd[0] == -1:
                        pass
                elif graph[x][y] == 2:
                    if dd[0] == 1 or dd[0] == -1:
                        dd = (0, 0)
                    elif dd[1] == 1 or dd[1] == -1:
                        pass
                elif graph[x][y] == 3:
                    # 빨간선
                    if dd[0] == 1 and dd[1] == 0:
                        dd = (0, -1)
                    # 초록선
                    elif dd[0] == 0 and dd[1] == -1:
                        dd = (1, 0)
                    # 보라선
                    elif dd[0] == -1 and dd[1] == 0:
                        dd = (0, 1)
                    # 파란선
                    elif dd[0] == 0 and dd[1] == 1:
                        dd = (-1, 0)
                elif graph[x][y] == 4:
                    # 빨간선
                    if dd[0] == 0 and dd[1] == -1:
                        dd = (-1, 0)
                    # 초록선
                    elif dd[0] == -1 and dd[1] == 0:
                        dd = (0, -1)
                    # 보라선
                    elif dd[0] == 0 and dd[1] == 1:
                        dd = (1, 0)
                    # 파란선
                    elif dd[0] == 1 and dd[1] == 0:
                        dd = (0, 1)

                dx = x + dd[0]
                dy = y + dd[1]

                dfs(graph, visited, dx, dy, dd)
    return

def check_place(graph, air_conditioners):
    global n, m

    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))
    visited = [[False] * m for _ in range(n)]

    for x, y in air_conditioners:
        visited[x][y] = True

        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            dfs(graph, visited, dx, dy, d)

    place_count = count_visit(visited)

    return place_count

def count_visit(visited):
    global n, m

    count = 0

    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                count += 1

    return count

if __name__ == "__main__":
    n, m = list(map(int, input().split()))

    graph = []
    air_conditioners = []

    for i in range(n):
        temp = list(map(int, input().split()))

        graph.append(temp)

        for j in range(m):
            if temp[j] == 9:
                air_conditioners.append((i, j))


    # print(*graph, sep='\n')
    # print(air_conditioner)

    print(check_place(graph, air_conditioners))

