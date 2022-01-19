"""
Date    : 2021.12.01
Update  : 2021.12.01
Source  : Q43_어두운 길.py
Purpose : 크루스칼 알고리즘 적용하여 해결.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
# 각 집 사이의 거리가 최소인 길만 가로등을 켠다. -> 크루스칼 알고리즘
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

n, m = list(map(int, input().split()))

roots = []
# 집의 번호가 0 ~ N-1번으로 주어졌기 때문에 parent의 원소 갯수를 n개만 생성함.
parent = [0] * n
save_cost = 0

for _ in range(m):
    x, y, z = list(map(int, input().split()))
    # 크루스칼 알고리즘을 사용하기 위해(비용 순으로 정렬하기 위해), 길에 대한 정보를 바꿔서 roots 리스트에 집어넣음.
    roots.append((z, x, y))
# 최소 비용의 길부터 탐색하기 위해 첫번째 원소를 기준으로 정렬을 함.
roots.sort()

# 초기 각 집의 부모를 자기 자신으로 초기화함.
for i in range(1, n):
    parent[i] = i

for root in roots:
    cost, a, b = root
    # 부모가 같지 않다면(싸이클이 없다면) union 연산을 함.
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    else:
        # 문제에서 구하고자 하는 값이 가로등을 비활성하여 절약할 수 있는 금액임.
        # 따라서 가로등을 켜지 않는 경우를 누적하여 합함.
        save_cost += cost

print(save_cost)
