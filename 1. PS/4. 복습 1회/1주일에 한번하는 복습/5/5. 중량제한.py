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

def check_max_weight(bridges):
    parent = [i for i in range(n)]

    for bridge in bridges:
        weight, a_island, b_island = bridge

        union_parent(parent, a_island, b_island)

        if find_parent(parent, src) == find_parent(parent, dest):
            max_weight = weight
            break

    return max_weight

if __name__ == "__main__":
    n, m = list(map(int, input().split()))

    bridges = []

    for _ in range(m):
        a_island, b_island, weight = list(map(int, input().split()))
        bridges.append((weight, a_island-1, b_island-1))

    src, dest = list(map(lambda x: int(x)-1, input().split()))

    bridges.sort(key=lambda x: -x[0])

    print(check_max_weight(bridges))