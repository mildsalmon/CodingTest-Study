"""
Date    : 2021.12.23
Update  : 2021.12.23
Source  : 21922.py
Purpose :
url     : https://www.acmicpc.net/problem/5567
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def wind_move(graph, visited, x, y):
    """
    바람이 지나가는 자리를 구함.
    :param graph:
    :param visited: 방문한 위치 (mutable 객체라 따로 return하지 않음)
    :param x: 에어컨 x좌표
    :param y: 에어컨 y좌표
    :return:
    """
    global n, m

    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))
    # 이 부분은 블로그에 그림으로 설명할 예정
    item = {1:(9, 1, 9, 3),
            2:(0, 9, 2, 9),
            3:(3, 2, 1, 0),
            4:(1, 0, 3, 2)}

    for i in range(4):
        d = ds[i]

        dx = x + d[0]
        dy = y + d[1]

        while True:
            # 연구실을 벗어나는 경우
            if 0 <= dx < n and 0 <= dy < m:
                # 현재 위치가 에어컨이 아닌 경우
                if graph[dx][dy] != 9:
                    visited[dx][dy] = True
                    # 현재 위치에 물건이 있는 경우
                    if graph[dx][dy] in (1, 2, 3, 4):
                        i = item[graph[dx][dy]][i]
                        # 물건1, 물건2로 인해 더 이상 이동하지 못하는 경우
                        if i == 9:
                            break
                        else:
                            d = ds[i]

                    dx += d[0]
                    dy += d[1]
                else:
                    break
            else:
                break
    return

def check_place(graph, air_conditioners) -> int:
    """
    에어컨별로 바람의 경로를 구함.
    :param graph:
    :param air_conditioners:
    :return: 바람이 지나가는 자리의 수
    """
    global n, m

    visited = [[False] * m for _ in range(n)]

    for x, y in air_conditioners:
        visited[x][y] = True

        wind_move(graph, visited, x, y)

    return count_visit(visited)

def count_visit(visited) -> int:
    """
    바람이 지나가는 자리의 갯수를 구함
    :param visited: 바람이 지나가면 true
    :return: 바람이 지나가는 자리의 수
    """
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

