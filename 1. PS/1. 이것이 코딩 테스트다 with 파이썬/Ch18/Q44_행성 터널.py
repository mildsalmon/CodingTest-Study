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

planets = []
tunnels = []
parent = [i for i in range(n)]
total_cost = 0

for i in range(n):
    x_a, y_a, z_a = list(map(int, input().split()))

    if i >= 1:
        for j in range(len(planets)):
            x_b, y_b, z_b = planets[j]

            cost = min(abs(x_a - x_b), abs(y_a - y_b), abs(z_a - z_b))
            tunnels.append((cost, i, j))

    planets.append((x_a, y_a, z_a))

tunnels.sort()

for tunnel in tunnels:
    cost, a, b = tunnel

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

print(total_cost)