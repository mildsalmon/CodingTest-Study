"""
Date    : 2022.01.26
Update  : 2022.01.26
Source  : 1717.py
Purpose :
url     : https://www.acmicpc.net/problem/1717
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(100_000)


def find_parent(parent: list, x: int) -> int:
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent: list, a: int, b: int) -> None:
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    elif a < b:
        parent[b] = a


if __name__ == "__main__":
    n, m = list(map(int, input().split()))

    parent = [i for i in range(n+1)]

    for _ in range(m):
        check, a, b = list(map(int, input().split()))

        if check:
            if find_parent(parent, a) == find_parent(parent, b):
                print("YES")
            else:
                print("NO")
        else:
            union_parent(parent, a, b)