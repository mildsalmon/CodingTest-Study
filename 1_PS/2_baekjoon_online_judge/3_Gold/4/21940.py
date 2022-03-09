"""
Date    : 2022.03.09
Update  : 2022.03.09
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

    for i in range(n+1):
        graph[i][i] = 0

    for _ in range(m):
        a, b, cost = list(map(int, input().split()))

        graph[a][b] = cost

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    k = int(input())
    friends = list(map(int, input().split()))
    citys = []

    for i in range(1, n+1):
        max_cost = 0
        for j in friends:
            max_cost = max(max_cost, graph[j][i] + graph[i][j])
        citys.append([max_cost, i])

    citys.sort(key=lambda x: [x[0], x[1]])

    # print(*graph, sep='\n')
    # print(citys)

    for city in citys:
        if city[0] == citys[0][0]:
            print(city[1], end=' ')
