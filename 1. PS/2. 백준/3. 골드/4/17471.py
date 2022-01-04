"""
Date    : 2022.01.04
Update  : 2022.01.04
Source  : 17471.py
Purpose :
url     : https://www.acmicpc.net/problem/17471
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from collections import deque


def bfs(leaf_city):
    global populations, graph

    visited = [False] * n

    q = deque()
    q.append(leaf_city)

    visited[leaf_city] = True

    A_city_population = populations[leaf_city]
    B_city_population = sum(populations) - A_city_population

    diff_city_population = -1

    while q:
        now_city = q.popleft()

        for next_city in graph[now_city]:
            if not visited[next_city]:
                diff_city_population = abs(A_city_population - B_city_population)

                A_city_population = A_city_population + populations[next_city]
                B_city_population = B_city_population - populations[next_city]

                if diff_city_population < abs(A_city_population - B_city_population):
                    return diff_city_population
                else:
                    diff_city_population = abs(A_city_population - B_city_population)


                visited[next_city] = True
                q.append(next_city)


    return diff_city_population


if __name__ == "__main__":
    n = int(input())
    populations = list(map(int, input().split()))

    graph = [[] for _ in range(n)]

    leaf_city = 0
    root_city = 0

    for i in range(n):
        temp = list(map(int, input().split()))

        for j in range(1, temp[0]+1):
            graph[i].append(temp[j]-1)

        if len(graph[i]) > len(graph[root_city]):
            root_city = i

        if len(graph[i]) == len(graph[leaf_city]):
            if populations[i] < populations[leaf_city]:
                leaf_city = i
        elif len(graph[i]) < len(graph[leaf_city]):
            leaf_city = i

    print(bfs(leaf_city))
