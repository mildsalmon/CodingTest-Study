"""
Date    : 2022.03.07
Update  : 2022.03.11
Source  : 21937.py
Purpose : dfs / bfs
url     : https://www.acmicpc.net/problem/21937
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(x, works):
    global graph

    if len(graph[x]) == 0:
        return

    for next_x in graph[x]:
        if next_x in works:
            continue
        works.add(next_x)
        dfs(next_x, works)


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]

    for i in range(m):
        a, b = list(map(int, input().split()))

        graph[b].append(a)

    x = int(input())
    works = set()

    dfs(x, works)

    print(len(works))