"""
Date    : 2022.01.10
Update  : 2022.01.10
Source  : 4. 게리맨더링.py
Purpose :
url     : https://www.acmicpc.net/problem/17471
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from itertools import combinations

def check_party(party):
    global graph, n

    visited = [False] * n

    for city in party:
        for next_city in graph[city]:
            if next_city in party:
                visited[next_city] = True

    return len(party) == visited.count(True)

def sum_population(party):
    global population

    count = 0

    for city in party:
        count += population[city]

    return count

if __name__ == "__main__":
    n = int(input())
    population = list(map(int, input().split()))

    graph = []

    for i in range(n):
        _, *temp = list(map(int, input().split()))

        for j in range(len(temp)):
            temp[j] -= 1

        graph.append(temp)

    answer = 1e9

    for i in range(1, n//2+1):
        A_partys = set(combinations(range(n), i))
        for A_party in A_partys:
            B_party = set(range(n)).difference(A_party)

            if check_party(A_party) and check_party(B_party):
                # print(f"{A_party} | {B_party}")
                answer = min(answer, abs(sum_population(A_party) - sum_population(B_party)))

    if answer == 1e9:
        print(-1)
    else:
        print(answer)