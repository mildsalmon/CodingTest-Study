# # 팀 결성
#
# def find(parent, x):
#     if parent[x] != x:
#         parent[x] = find(parent, parent[x])
#     return parent[x]
#
# def union(parent, a, b):
#     a = find(parent, a)
#     b = find(parent, b)
#
#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a
#
# n, m = list(map(int, input().split()))
#
# parent = [i for i in range(n+1)]
#
# # print(parent)
# answer = []
# for i in range(m):
#     c, a, b = list(map(int, input().split()))
#
#     if c == 0:
#         union(parent, a, b)
#     else:
#         if find(parent, a) == find(parent, b):
#             answer.append("YES")
#         else:
#             answer.append("NO")
#
# print(*answer, sep='\n')
#
# # 7 8
# # 0 1 3
# # 1 1 7
# # 0 7 6
# # 1 7 1
# # 0 3 7
# # 0 4 2
# # 0 1 1
# # 1 1 1

# 도시 분할 계획

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = list(map(int, input().split()))

town = [i for i in range(n+1)]
distance = []

for i in range(m):
    a, b, c = list(map(int, input().split()))

    distance.append([c, a, b])

distance.sort()

answer = 0
for i in distance:
    if find(town, i[1]) != find(town, i[2]):
        union(town, i[1], i[2])
        answer += i[0]
        last = i[0]

print(answer - last)