# # Ch10_그래프_팀 결성
#
# def find(team, x):
#     if team[x] != x:
#         team[x] = find(team, team[x])
#     return team[x]
#
# def union(team, a, b):
#     a = find(team, a)
#     b = find(team, b)
#
#     if a < b:
#         team[b] = a
#     else:
#         team[a] = b
#
# n, m = list(map(int, input().split()))
#
# team = [i for i in range(n+1)]
#
# answer = []
#
# for i in range(m):
#     c, a, b = list(map(int, input().split()))
#
#     if c == 0:
#         union(team, a, b)
#     if c == 1:
#         if find(team, a) == find(team, b):
#             answer.append("YES")
#         else:
#             answer.append("NO")
#
# print(*answer, sep='\n')
#
# # 9분 / pass

# Ch10_그래프_도시 분할 계획

def find(house, x):
    if house[x] != x:
        house[x] = find(house, house[x])
    return house[x]

def union(house, a, b):
    a = find(house, a)
    b = find(house, b)

    if a < b:
        house[b] = a
    else:
        house[a] = b

n, m = list(map(int, input().split()))
array = []
house = [i for i in range(n+1)]
answer = []

for i in range(m):
    a, b, c = list(map(int, input().split()))

    array.append((c, a, b))

array.sort()

for i in array:
    c, a, b = i
    # print(house)
    if find(house, a) != find(house, b):
        union(house, a, b)
        answer.append(c)

print(sum(answer) - max(answer))