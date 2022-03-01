"""
Date    : 2022.03.02
Update  : 2022.03.02
Source  : 21924.py
Purpose :
url     : https://www.acmicpc.net/problem/21924
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys

input = sys.stdin.readline


def find_parent(parent: list, x: int) -> int:
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent: list, a: int, b: int):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    elif a < b:
        parent[b] = a


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    ways = []
    total_cost = 0

    for i in range(m):
        a, b, c = list(map(int, input().split()))
        total_cost += c
        ways.append((c, a, b))

    ways.sort()

    parent = [i for i in range(n+1)]

    for cost, a, b in ways:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            total_cost -= cost

    for i in range(1, n+1):
        if parent[i] != 1:
            find_parent(parent, i)

    if sum(parent) == n:
        print(total_cost)
    else:
        print(-1)