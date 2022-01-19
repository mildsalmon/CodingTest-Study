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

def check_plan(parent, plan):
    for i in range(1, len(plan)):
        if find_parent(parent, plan[i - 1]) != find_parent(parent, plan[i]):
            print("NO")
            return
    print("YES")
    return

n, m = list(map(int, input().split()))

graph = [[] for i in range(n+1)]
parent = [i for i in range(n+1)]

for i in range(n):
    temp = list(map(int, input().split()))

    for j in range(n):
        if temp[j] == 1:
            graph[i+1].append(j+1)

plan = list(map(int, input().split()))

for i in range(1, n+1):
    for j in graph[i]:
        union_parent(parent, i, j)

check_plan(parent, plan)
