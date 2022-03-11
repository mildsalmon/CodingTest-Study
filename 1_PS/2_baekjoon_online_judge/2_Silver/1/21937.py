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
from collections import deque

sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def bfs(x, works):
    global graph

    if len(graph[x]) == 0:
        return

    q = deque()
    q.append(x)

    while q:
        node = q.popleft()

        for next_x in graph[node]:
            if next_x in works:
                continue
            works.add(next_x)
            q.append(next_x)


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]

    for i in range(m):
        a, b = list(map(int, input().split()))

        graph[b].append(a)

    x = int(input())
    works = set()

    bfs(x, works)

    print(len(works))