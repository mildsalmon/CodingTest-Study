# # Ch10_그래프 이론_팀 결성
#
# def find(team, x):
#     if team[x] != x:
#         team[x] = find(team, team[x])
#
#     return team[x]
#
# def union(team, a, b):
#     a = find(team, a)
#     b = find(team, b)
#
#     if a > b:
#         team[a] = b
#     else:
#         team[b] = a
#
# n, m = list(map(int, input().split()))
#
# array = []
# team = [i for i in range(n+1)]
# answer = []
#
# for i in range(m):
#     c, a, b = list(map(int, input().split()))
#
#     if c == 0:
#         union(team, a, b)
#     elif c == 1:
#         if find(team, a) == find(team, b):
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
#
# # 13분 / pass
#

# Ch10_그래프 이론_도시 분할 계획

def find(house, x):
    if house[x] != x:
        house[x] = find(house, house[x])
    return house[x]

def union(house, a, b):
    a = find(house, a)
    b = find(house, b)

    if a > b:
        house[a] = b
    else:
        house[b] = a


n, m = list(map(int, input().split()))
house = [i for i in range(n+1)]
array = []
answer = 0

for i in range(m):
    a, b, c = list(map(int, input().split()))
    array.append([c, a, b])

array.sort()

for i in array:
    c, a, b = i

    if find(house, a) != find(house, b):
        union(house, a, b)
        answer += c
        max_c = c
print(answer - max_c)

# 14분 / pass
