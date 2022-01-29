"""
Date    : 2022.01.29
Update  : 2022.01.29
Source  : 16954.py
Purpose :
url     : https://www.acmicpc.net/problem/16954
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":
    graph = []

    for _ in range(8):
        temp = list(input())
        graph.append(temp)

    visited = [[False] * 8 for _ in range(8)]
    visited[7][0] = True

    for i in range(8):
        for x in range(8-i):
            for y in range(8):
                if graph[x][y] == '#':
                    visited[x+i][y] = False

        temp_visited = [[False] * 8 for _ in range(8)]

        for j in range(8):
            for k in range(8):
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if 0 <= j+x < 8 and 0 <= k+y < 8 and visited[j+x][k+y]:
                            temp_visited[j][k] = True

        for j in range(8-i):
            for k in range(8):
                if graph[j][k] == '#':
                    temp_visited[j+i][k] = False

        visited = temp_visited

    if sum(map(sum, visited)):
        print(1)
    else:
        print(0)