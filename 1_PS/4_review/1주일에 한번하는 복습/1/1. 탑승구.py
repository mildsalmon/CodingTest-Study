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

g = int(input())
p = int(input())

gates = []

for i in range(p):
    gates.append(int(input()))

parent = [i for i in range(g+1)]
count = 0

for gate in gates:
    if find_parent(parent, gate) == 0:
        break

    union_parent(parent, gate, find_parent(parent, gate)-1)
    count += 1

print(count)