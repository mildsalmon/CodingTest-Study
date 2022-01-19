"""
Date    : 2022.01.04
Update  : 2022.01.04
Source  : 17471.py
Purpose : bfs / set(difference) / combination
url     : https://www.acmicpc.net/problem/17471
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from collections import deque
from itertools import combinations

def check_area_connect(area) -> bool:
    global n, graph

    q: deque = deque()
    q.append(area[0])

    visited: list = [False] * n
    visited[area[0]] = True

    while q:
        city: int = q.popleft()

        # area에 있는 city들이 연결되는지 체크
        for next_city in graph[city]:
            if next_city in area:
                if not visited[next_city]:
                    visited[next_city] = True
                    q.append(next_city)

    return len(area) == visited.count(True)

def sum_population(area) -> int:
    global populations

    # result = 0
    #
    # for a in area:
    #     result += populations[a]

    # return result

    return sum(map(lambda x: populations[x], area))


if __name__ == "__main__":
    n: int = int(input())
    populations: list = list(map(int, input().split()))

    citys: set = {i for i in range(n)}
    graph: list = [[] for _ in range(n)]

    for i in range(n):
        temp: list = list(map(int, input().split()))

        for j in range(1, temp[0]+1):
            graph[i].append(temp[j]-1)

    diff_population: int = 1e9

    # range가 1부터 시작
        # 각 선거구는 하나의 구역을 포함해야한다.
    # range가 n//2 + 1로 끝난다.
        # 6C2 = 6C4는 같다. A선거구가 2개 지역을 먹든, 2개 지역을 안먹든 동일하다.
    for i in range(1, n//2+1):
        A_areas = list(combinations(range(n), i))

        for A_area in A_areas:
            # 선택되지 않은 지역들을 B지역으로 지정.
            B_area = tuple(citys.difference(A_area))

            if check_area_connect(A_area) and check_area_connect(B_area):
                A_population = sum_population(A_area)
                B_population = sum_population(B_area)

                diff_population = min(diff_population, abs(A_population - B_population))

    if diff_population == 1e9:
        print(-1)
    else:
        print(diff_population)

