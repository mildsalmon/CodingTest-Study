"""
Date    : 2022.04.08
Update  : 2022.04.08
Source  : 11724.py
Purpose : dfs / 그래프 탐색 / 그래프
url     : https://www.acmicpc.net/problem/11724
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(i, visited):
    global graph

    visited[i] = True

    for next_node in graph[i]:
        if not visited[next_node]:
            dfs(next_node, visited)


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]

    for i in range(m):
        a, b = list(map(int, input().split()))

        graph[a].append(b)
        graph[b].append(a)

    visited = [False for _ in range(n+1)]
    cnt = 0

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i, visited)
            cnt += 1

    print(cnt)