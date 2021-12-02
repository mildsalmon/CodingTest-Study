"""
Date    : 2021.12.02
Update  : 2021.12.02
Source  : Q44_행성 터널.py
Purpose : 각 좌표별로 분리하고, 크루스칼 알고리즘 적용하여 해결.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())

# 행성별 x, y, z 좌표를 따로 저장한다.
planets_x = []
planets_y = []
planets_z = []

# x, y, z별로 구한 최소 비용을 tunnels에 저장한다.
tunnels = []

# 최소거리별로 그룹지어 줄 parent를 생성하고 자신의 인덱스로 초기화한다.
parent = [i for i in range(n)]

# 결과로 출력할 최소 비용의 합
total_cost = 0

for i in range(n):
    x, y, z = list(map(int, input().split()))

    planets_x.append((x, i))
    planets_y.append((y, i))
    planets_z.append((z, i))

# 각 좌표를 정렬한다.
# 이 정렬을 통해, 모든 행성에 대해 최소 거리를 구하는 것이 아닌, 바로 옆에 있는 행성과 계산하여 최소 거리를 구한다.
planets_x.sort()
planets_y.sort()
planets_z.sort()

for i in range(n-1):
    tunnels.append((planets_x[i+1][0] - planets_x[i][0], planets_x[i][1], planets_x[i+1][1]))
    tunnels.append((planets_y[i+1][0] - planets_y[i][0], planets_y[i][1], planets_y[i+1][1]))
    tunnels.append((planets_z[i+1][0] - planets_z[i][0], planets_z[i][1], planets_z[i+1][1]))

# 크루스칼 알고리즘을 위해 정렬.
tunnels.sort()

for tunnel in tunnels:
    cost, a, b = tunnel

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

print(total_cost)