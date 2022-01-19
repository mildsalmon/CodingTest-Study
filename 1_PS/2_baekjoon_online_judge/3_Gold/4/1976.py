"""
Date    : 2022.01.13
Update  : 2022.01.13
Source  : 1976.py
Purpose : union-parent / 그래프
url     : https://www.acmicpc.net/problem/1976
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a > b:
        parent[a] = b
    elif a < b:
        parent[b] = a

def check_plan(plan, parent):
    for i in range(1, len(plan)):
        if find(parent, plan[i-1]) != find(parent, plan[i]):
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n)]
    parent = [i for i in range(n)]

    for i in range(n):
        temp = list(map(int, input().split()))

        for j, value in enumerate(temp):
            if value == 1:
                if find(parent, i) != find(parent, j):
                    union(parent, i, j)

    plan = list(map(lambda x: int(x)-1, input().split()))

    if check_plan(plan, parent):
        print("YES")
    else:
        print("NO")