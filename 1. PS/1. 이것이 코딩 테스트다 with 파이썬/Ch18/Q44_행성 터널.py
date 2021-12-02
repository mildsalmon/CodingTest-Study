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

planets_x = []
planets_y = []
planets_z = []
tunnels = []
parent = [i for i in range(n)]
total_cost = 0

for i in range(n):
    x, y, z = list(map(int, input().split()))

    planets_x.append((x, i))
    planets_y.append((y, i))
    planets_z.append((z, i))

planets_x.sort()
planets_y.sort()
planets_z.sort()

for i in range(n-1):
    tunnels.append((planets_x[i+1][0] - planets_x[i][0], planets_x[i][1], planets_x[i+1][1]))
    tunnels.append((planets_y[i+1][0] - planets_y[i][0], planets_y[i][1], planets_y[i+1][1]))
    tunnels.append((planets_z[i+1][0] - planets_z[i][0], planets_z[i][1], planets_z[i+1][1]))

tunnels.sort()

for tunnel in tunnels:
    cost, a, b = tunnel

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

print(total_cost)