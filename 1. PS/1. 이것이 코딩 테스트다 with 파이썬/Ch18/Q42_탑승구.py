"""
Date    : 2021.11.30
Update  : 2021.11.30
Source  : Q42_탑승구.py
Purpose : union-find 알고리즘 적용하여 해결.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])

    return parent[node]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b

g = int(input())
p = int(input())

boarding_gate = []

for _ in range(p):
    boarding_gate.append(int(input()))

docking = [i for i in range(g+1)]
count = 0

for b_g in boarding_gate:
    parent = find_parent(docking, b_g)

    if parent == 0:
        break
    else:
        union_parent(docking, parent, parent-1)
        count += 1

print(count)