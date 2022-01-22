"""
Date    : 2022.01.22
Update  : 2022.01.22
Source  : 6. 게리맨더링.py
Purpose :
url     : https://www.acmicpc.net/problem/17471
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from itertools import combinations
from collections import deque


def check_connect(party):
    global area, n

    visited = [False] * n
    visited[party[0]] = True

    q = deque()
    q.append(party[0])

    while q:
        city = q.popleft()

        for next_city in area[city]:
            if not visited[next_city]:
                if next_city in party:
                    visited[next_city] = True
                    q.append(next_city)

    return visited.count(True) == len(party)


def population_party(party):
    global populations

    return sum(map(lambda x: populations[x], party))


if __name__ == "__main__":
    n = int(input())
    populations = list(map(int, input().split()))
    area = []

    diff_population = 1e9

    for _ in range(n):
        _, *temp = list(map(lambda x: int(x)-1, input().split()))
        area.append(temp)

    for i in range(1, n//2+1):
        A_partys = list(combinations(range(n), i))

        for A_party in A_partys:
            B_party = list(set(range(n)).difference(A_party))

            if check_connect(A_party) and check_connect(B_party):
                diff_population = min(diff_population, abs(population_party(A_party) - population_party(B_party)))

    if diff_population == 1e9:
        print(-1)
    else:
        print(diff_population)
