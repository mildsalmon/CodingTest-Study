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

n = int(input())

x = []
y = []
z = []

for i in range(n):
    t_x, t_y, t_z = list(map(int, input().split()))

    x.append((t_x, i))
    y.append((t_y, i))
    z.append((t_z, i))

x.sort()
y.sort()
z.sort()

parent = [i for i in range(n)]
planets = []

for i in range(1, n):
    planets.append((x[i][0] - x[i-1][0], x[i][1], x[i-1][1]))
    planets.append((y[i][0] - y[i-1][0], y[i][1], y[i-1][1]))
    planets.append((z[i][0] - z[i-1][0], z[i][1], z[i-1][1]))

planets.sort()
minimum_cost = 0

for planet in planets:
    cost, a, b = planet

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        minimum_cost += cost

print(minimum_cost)
