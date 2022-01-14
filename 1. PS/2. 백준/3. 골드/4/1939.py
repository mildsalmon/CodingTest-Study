"""
Date    : 2022.01.14
Update  : 2022.01.14
Source  : 1939.py
Purpose :
url     : https://www.acmicpc.net/problem/1939
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from collections import deque

if __name__ == "__main__":
    # 섬, 다리
    n, m = list(map(int, input().split()))

    islands = [[] for _ in range(n)]

    for i in range(m):
        a, b, weight = list(map(int, input().split()))

        islands[a-1].append((weight, b-1))
        islands[b-1].append((weight, a-1))

    src, dest = list(map(lambda x: int(x)-1, input().split()))

    visited = [False] * n
    visited[src] = True

    q = deque([[1e9, src, visited]])

    max_root = -1e9

    while q:
        sub_root, now_island, temp_visited = q.popleft()

        if now_island == dest:
            max_root = max(max_root, sub_root)
            continue

        for next_weight, next_island in islands[now_island]:
            if not temp_visited[next_island]:
                acc_root = min(sub_root, next_weight)
                temp_visited[next_island] = True
                q.append([acc_root, next_island, temp_visited[:]])
                temp_visited[next_island] = False

    print(max_root)