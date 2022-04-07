"""
Date    : 2022.04.07
Update  : 2022.04.07
Source  : 2667.py
Purpose : dfs / 탐색 / 그래프
url     : https://www.acmicpc.net/problem/2667
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def dfs(i, j, visited):
    global area, n, cnt

    ds = ((0, 1), (0, -1), (1, 0), (-1, 0))

    visited[i][j] = True
    cnt += 1

    for d in ds:
        dx = i + d[0]
        dy = j + d[1]

        if 0 <= dx < n and 0 <= dy < n:
            if visited[dx][dy]:
                continue
            if area[dx][dy] == '1':
                dfs(dx, dy, visited)


if __name__ == "__main__":
    global area, n, cnt

    answer = []
    n = int(input())
    area = [list(input()) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            cnt = 0

            if not visited[i][j] and area[i][j] == '1':
                dfs(i, j, visited)
                answer.append(cnt)

    answer.sort()
    print(len(answer))
    print(*answer, sep='\n')