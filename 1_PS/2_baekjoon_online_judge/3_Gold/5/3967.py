"""
Date    : 2022.03.16
Update  : 2022.03.16
Source  : 3967.py
Purpose :
url     : https://www.acmicpc.net/problem/3967
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def convert(chr):
    return ord(chr) - ord('A')


def reverse_convert(num):
    return chr(num + ord('A'))


def search_magic_star(depth, visited, stars):
    global graph, answer, cnt

    if cnt == depth:
        if convert(graph[0][4]) + convert(graph[1][5]) + convert(graph[2][6]) + convert(graph[3][7]) + 4 != 26:
            return False
        if convert(graph[1][7]) + convert(graph[2][6]) + convert(graph[3][5]) + convert(graph[4][4]) + 4 != 26:
            return False
        if convert(graph[3][1]) + convert(graph[3][3]) + convert(graph[3][5]) + convert(graph[3][7]) + 4 != 26:
            return False
        if convert(graph[4][4]) + convert(graph[3][3]) + convert(graph[2][2]) + convert(graph[1][1]) + 4 != 26:
            return False
        if convert(graph[3][1]) + convert(graph[2][2]) + convert(graph[1][3]) + convert(graph[0][4]) + 4 != 26:
            return False
        if convert(graph[1][1]) + convert(graph[1][3]) + convert(graph[1][5]) + convert(graph[1][7]) + 4 != 26:
            return False
        return True

    for i in range(12):
        if visited[i]:
            continue
        x, y = stars[depth]
        graph[x][y] = reverse_convert(i)
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
                else:
                    stars.append((i, j))

    cnt = len(stars)

    search_magic_star(0, visited, stars)

    for i in range(5):
        print(''.join(graph[i]))