"""
Date    : 2022.01.14
Update  : 2022.01.14
Source  : 1939.py
Purpose : 이진탐색 / bfs / union-find / heap / sys 속도 체감
url     : https://www.acmicpc.net/problem/1939
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import heapq
import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    elif a < b:
        parent[b] = a

if __name__ == "__main__":
    # 섬, 다리
    n, m = list(map(int, input().split()))

    bridges = []

    for i in range(m):
        a, b, weight = list(map(int, input().split()))

        heapq.heappush(bridges, (-weight, a-1, b-1))

    src, dest = list(map(lambda x: int(x) - 1, input().split()))

    parent = [i for i in range(n)]

    while bridges:
        current_weight, current_a, current_b = heapq.heappop(bridges)

        union_parent(parent, current_a, current_b)
        if find_parent(parent, src) == find_parent(parent, dest):
            print(-current_weight)
            break