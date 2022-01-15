"""
Date    : 2022.01.15
Update  : 2022.01.15
Source  : 1939.py
Purpose : 이진탐색 / bfs / union-find / heap / sys 속도 체감
url     : https://www.acmicpc.net/problem/1939
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys
from collections import deque

input = sys.stdin.readline

def bfs(mid: int) -> bool:
    global islands, src, dest, n

    q = deque()
    q.append(src)

    visited = [False] * n
    visited[src] = True

    while q:
        node = q.popleft()

        if visited[dest]:
            break

        for island in islands[node]:
            weight, a = island

            if not visited[a] and weight >= mid:
                visited[a] = True
                q.append(a)

    return visited[dest]

def binary_search(start: int, end: int) -> int:
    max_weight = 0

    while start <= end:
        mid = (start + end) // 2

        if bfs(mid):
            max_weight = mid
            start = mid + 1
        else:
            end = mid - 1

    return int(max_weight)

if __name__ == "__main__":
    n, m = list(map(int, input().split()))

    islands = [[] for _ in range(n)]

    for _ in range(m):
        a_island, b_island, weight = list(map(int, input().split()))

        islands[b_island-1].append((weight, a_island-1))
        islands[a_island-1].append((weight, b_island-1))

    src, dest = list(map(lambda x: int(x)-1, input().split()))

    print(binary_search(1, 1e9))