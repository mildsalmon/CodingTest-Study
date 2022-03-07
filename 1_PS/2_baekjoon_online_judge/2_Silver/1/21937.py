"""
Date    : 2022.03.07
Update  : 2022.03.07
Source  : 21937.py
Purpose : dfs / bfs
url     : https://www.acmicpc.net/problem/21937
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node: int):
    global answer, graph, visited

    visited[node] = True

    for next_node in graph[node]:
        if visited[next_node]:
            continue

        answer += 1
        dfs(next_node)


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]

    for _ in range(m):
        a, b = list(map(int, input().split()))
        graph[b].append(a)

    x = int(input())
    answer = 0
    dfs(x)

    print(answer)