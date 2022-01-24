"""
Date    : 2022.01.24
Update  : 2022.01.24
Source  : 1922.py
Purpose : union-parent / kruskal / graph
url     : https://www.acmicpc.net/problem/1922
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys

input = sys.stdin.readline


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
    n = int(input())
    m = int(input())
    lines = []
    parent = [i for i in range(n)]

    for _ in range(m):
        a, b, cost = list(map(int, input().split()))

        lines.append((cost, a-1, b-1))

    lines.sort()

    total_cost = 0
    cnt = 0

    for line in lines:
        cost, a, b = line

        # edge의 수는 '전체 node 갯수 - 1'
        if cnt == n-1:
            break

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            total_cost += cost
            cnt += 1


    print(total_cost)