"""
Date    : 2022.01.15
Update  : 2022.01.15
Source  : 17471.py
Purpose : bfs / set
url     : https://www.acmicpc.net/problem/1520
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from itertools import combinations
from collections import deque

def possible_sector(sector):
    global graph, n

    visited = [False] * n
    visited[sector[0]] = True

    q = deque()
    q.append(sector[0])

    while q:
        city = q.popleft()

        for next_node in graph[city]:
            if next_node in sector:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node)

    return len(sector) == visited.count(True)

def diff_population(A_sector, B_sector):
    return abs(sum_population(A_sector) - sum_population(B_sector))

def sum_population(sector):
    global populations

    result = 0

    for city in sector:
        result += populations[city]

    return result

if __name__ == "__main__":
    n = int(input())
    populations = list(map(int, input().split()))

    graph = []

    for i in range(n):
        _, *temp = list(map(lambda x: int(x)-1, input().split()))
        graph.append(temp)

    min_diff_population = 1e9

    # combination에서
        # r=0이면, 아무것도 선택되지 않는다.
        # r=n-r은 같다.
    for r in range(1, n//2+1):
        A_sectors = combinations(range(n), r)

        for A_sector in A_sectors:
            B_sector = tuple({*range(n)}.difference(A_sector))

            if possible_sector(A_sector) and possible_sector(B_sector):
                min_diff_population = min(min_diff_population, diff_population(A_sector, B_sector))

    if min_diff_population == 1e9:
        print(-1)
    else:
        print(min_diff_population)