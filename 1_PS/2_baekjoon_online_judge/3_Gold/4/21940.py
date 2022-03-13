"""
Date    : 2022.03.09
Update  : 2022.03.13
Source  : 21940.py
Purpose : 플로이드-와샬
url     : https://www.acmicpc.net/problem/21940
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    graph = [[1e9] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        graph[i][i] = 0

    for _ in range(m):
        a, b, time = list(map(int, input().split()))

        graph[a][b] = time

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # print(*graph, sep='\n')

    k = int(input())
    c = list(map(int, input().split()))

    dest_citys = []
    min_distance = 1e9

    for i in range(1, n+1):
        max_distance = 0

        for j in c:
            max_distance = max(max_distance, graph[i][j] + graph[j][i])

        if min_distance < max_distance:
            continue
        elif min_distance > max_distance:
            min_distance = max_distance
            dest_citys = []
        dest_citys.append(i)
    dest_citys.sort()

    print(*dest_citys, sep=' ')
