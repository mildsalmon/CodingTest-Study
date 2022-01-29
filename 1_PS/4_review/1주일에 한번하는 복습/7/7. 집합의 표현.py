"""
Date    : 2022.01.29
Update  : 2022.01.29
Source  : 1717.py
Purpose : union-find / recursive
url     : https://www.acmicpc.net/problem/1717
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


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
    n, m = list(map(int, input().split()))

    parents = [i for i in range(n+1)]

    for _ in range(m):
        decision, a, b = list(map(int, input().split()))

        if decision:
            if find_parent(parents, a) == find_parent(parents, b):
                print("YES")
            else:
                print("NO")
        else:
            union_parent(parents, a, b)