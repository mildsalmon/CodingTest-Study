"""
Date    : 2022.01.20
Update  : 2022.01.20
Source  : 14503.py
Purpose :
url     : https://www.acmicpc.net/problem/14503
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def move(graph, x, y, d):
    global clean_area

    clean_area += 1
    graph[x][y] = 2

    dfs(graph, x, y, d)



def dfs(graph, x, y, d):
    ds = ((-1, 0), (0, 1), (1, 0), (0, -1))

    count = 0

    for i in range(4):
        d = (d - 1) % 4

        dx = x + ds[d][0]
        dy = y + ds[d][1]

        count += 1

        if graph[dx][dy] != 1:
            if graph[dx][dy] == 0:
                move(graph, dx, dy, d)

    if count == 4:
        dx = x - ds[d][0]
        dy = y - ds[d][1]

        if graph[dx][dy] == 1:
            print(clean_area)
            exit(0)
        else:
            dfs(graph, dx, dy, d)

    return False


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    r, c, d = list(map(int, input().split()))

    graph = []

    for _ in range(n):
        temp = list(map(int, input().split()))
        graph.append(temp)

    clean_area = 0

    move(graph, r, c, d)

