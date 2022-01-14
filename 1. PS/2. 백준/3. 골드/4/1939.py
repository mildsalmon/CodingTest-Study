"""
Date    : 2022.01.14
Update  : 2022.01.14
Source  : 1939.py
Purpose : 이진탐색 / bfs
url     : https://www.acmicpc.net/problem/1939
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from collections import deque

def bfs(max_root):
    global src, dest, n, islands

    q = deque()
    q.append(src)
    visited = [False] * n
    visited[src] = True

    while q:
        island = q.popleft()

        for next_weight, next_island in islands[island]:
            if not visited[next_island] and next_weight >= max_root:
                q.append(next_island)
                visited[next_island] = True

    return visited[dest]

def binary_search(max_root, min_root):
    result = min_root

    while min_root <= max_root:
        mid_root = (max_root + min_root) // 2

        check = bfs(mid_root)

        if check:
            result = mid_root
            min_root = mid_root + 1
        else:
            max_root = mid_root - 1

    return int(result)

if __name__ == "__main__":
    # 섬, 다리
    n, m = list(map(int, input().split()))

    islands = [[] for _ in range(n)]

    for i in range(m):
        a, b, weight = list(map(int, input().split()))

        islands[a-1].append((weight, b-1))
        islands[b-1].append((weight, a-1))

    src, dest = list(map(lambda x: int(x)-1, input().split()))

    max_root, min_root = 1e9, 1

    print(binary_search(max_root, min_root))
