# 이상 분할

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = 7, 12
v = ["1 2 3",
"1 3 2",
"3 2 1",
"2 5 2",
"3 4 4",
"7 3 6",
"5 1 5",
"1 6 2",
"6 4 1",
"6 5 3",
"4 5 3",
"6 7 4",]

# n, m = list(map(int, input().split()))
array = []
parent = [0] * (n+1)
result = 0
last = 0

for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    # a, b, c = list(map(int, input().split()))
    a, b, c = list(map(int, v[i].split()))
    array.append([c, a, b])

array.sort()

for i in range(m):
    c, a, b = array[i]

    if find_parent(parent, a) == find_parent(parent, b):
        continue
    else:
        union_parent(parent, a, b)
        result += c
        last = c
    print(parent[1:])

print(result-last)

# 22분 46초 / Non-Pass / 마지막 last = c를 생각 못함. (마을을 2덩어리로 나눈다고 했는데, 길 하나만 연결된 마을 2개인 줄 알았다.)