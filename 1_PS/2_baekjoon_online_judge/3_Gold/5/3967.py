"""
Date    : 2022.03.16
Update  : 2022.03.16
Source  : 3967.py
Purpose :
url     : https://www.acmicpc.net/problem/3967
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def convert(chr: str) -> int:
    return ord(chr) - ord('A')


def reverse_convert(num: int) -> str:
    return chr(num + ord('A'))


def search_magic_star(depth, visited, stars):
    global graph, answer, cnt

    if graph[0][4] != 'x' and graph[1][5] != 'x' and graph[2][6] != 'x' and graph[3][7] != 'x' and \
            graph[0][4] + graph[1][5] + graph[2][6] + graph[3][7] + 4 != 26:
        return False
    if graph[1][7] != 'x' and graph[2][6] != 'x' and graph[3][5] != 'x' and graph[4][4] != 'x' and\
            graph[1][7] + graph[2][6] + graph[3][5] + graph[4][4] + 4 != 26:
        return False
    if graph[3][1] != 'x' and graph[3][3] != 'x' and graph[3][5] != 'x' and graph[3][7] != 'x' and \
            graph[3][1] + graph[3][3] + graph[3][5] + graph[3][7] + 4 != 26:
        return False
    if graph[4][4] != 'x' and graph[3][3] != 'x' and graph[2][2] != 'x' and graph[1][1] != 'x' and \
            graph[4][4] + graph[3][3] + graph[2][2] + graph[1][1] + 4 != 26:
        return False
    if graph[3][1] != 'x' and graph[2][2] != 'x' and graph[1][3] != 'x' and graph[0][4] != 'x' and \
            graph[3][1] + graph[2][2] + graph[1][3] + graph[0][4] + 4 != 26:
        return False
    if graph[1][1] != 'x' and graph[1][3] != 'x' and graph[1][5] != 'x' and graph[1][7] != 'x' and \
            graph[1][1] + graph[1][3] + graph[1][5] + graph[1][7] + 4 != 26:
        return False

    if depth == cnt:
        return True

    x, y = stars[depth]
    for i in range(12):
        if visited[i]:
            continue
        graph[x][y] = i
        visited[i] = True
        flag = search_magic_star(depth+1, visited, stars)
        if flag:
            return True
        visited[i] = False
        graph[x][y] = 'x'


if __name__ == "__main__":
    graph = []
    # 방문한 지점 A ~ L은 0 ~ 11 index에 매핑
    visited = [False for _ in range(12)]
    stars = []
    answer = []

    for i in range(5):
        temp = list(input())
        graph.append(temp)
        for j in range(len(temp)):
            if temp[j] != '.':
                if temp[j] != 'x':
                    index = convert(temp[j])
                    visited[index] = True
                    graph[i][j] = convert(temp[j])
                else:
                    stars.append((i, j))

    cnt = len(stars)

    search_magic_star(0, visited, stars)

    for i in range(5):
        for j in range(len(graph[i])):
            if str(graph[i][j]).isdigit():
                print(reverse_convert(graph[i][j]), end='')
            else:
                print(graph[i][j], end='')
        print()