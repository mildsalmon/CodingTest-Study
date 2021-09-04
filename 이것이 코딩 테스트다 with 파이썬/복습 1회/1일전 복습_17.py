# #  CH10_그래프이론_팀 결성
#
# # 학생에게 0부터 N번까지 번호를 부여했다.
# # 모든 학생이 서로 다른 팀으로 구분되어 총 N+1개의 팀이 존재한다.
# # 팀 합치기 연산과 같은 팀 여부 확인 연산을 사용할 수 있다.
#
# # 팁 합치기
#     # 두 팀을 합치는 연산
# # 같은 팀 여부 확인
#     # 특정 두 학생이 같은 팀에 속하는지 확인
#
# # Input
#     # 첫째줄에 N, M
#         # 1 <= N, M <= 100,000
#     # 다음 M개 줄에 각각 연산이 주어진다.
#         # 팀 합치기는 0 a b (a 학생 팀과 b 학생 팀을 합친다)
#         # 같은 팀 여부 확인 1 a b (a학생과 b학생이 같은 팀이지 확인)
#         # a, b는 N 이하의 양의 정수
#
# # Output
#     # 같은 팀 여부 확인 연산에 대해 YES, NO를 한줄씩 출력
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
# array = []
# team = [0] * (n+1)
#
# for i in range(m):
#     c, a, b = list(map(int, input().split()))
#     array.append([c, a, b])
#
# for i in range(n+1):
#     team[i] = i
#
# for i in array:
#     c, a, b = i
#
#     if c == 0:
#         union(team, a, b)
#     elif c == 1:
#         if find(team, a) == find(team, b):
#             print("YES")
#         else:
#             print("NO")
#
# # 12분 3초 / Pass

# Ch10_그래프이론_도시 분할 계획

# 마을은 N개의 집과 집을 연결하는 M개의 길이 있다.
# 길은 어느 방향으로든 다닐 수 있다.
# 길을 유지하는데 유지비가 든다.

# 이장은 마을을 2개의 분리된 마을로 분할할 계획을 세운다.
# 각 분리된 마을 안에 집들은 서로 연결되어야 한다.
# 마음에는 집이 하나 이상 있어야 한다.

# 분리된 두 마일 사이의 길은 없앨 수 있다.
# 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있다.

# 위 조건을 만족하도록 길을 모우 없애고, 나머지 길의 유지비의 합을 최소로 하고 싶다.

# INput
    # 집의 개수 N, 길의 개수 M
        # 2 <= N <= 100,000
        # 1 <= M <= 1,000,000
    # M줄에 걸쳐 길의 정보 A, B, C가 공백으로 구분되어 주어진다.
        # A번 집과 B번 집을 연결하는 길의 유지비가 C(1<=C<=1,000)이다.

# Output
    # 길을 없애고 남은 유지비 합의 최솟값

def find(town, x):
    if town[x] != x:
        town[x] = find(town, town[x])
    return town[x]

def union(town, a, b):
    a = find(town, a)
    b = find(town, b)

    if a < b:
        town[b] = a
    else:
        town[a] = b

n, m = list(map(int, input().split()))

array = []

for i in range(m):
    a, b, c = list(map(int, input().split()))
    array.append([c, a, b])

town = [0] * (n+1)
result = 0

for i in range(1, n+1):
    town[i] = i

array.sort()

for i in array:
    c, a, b = i

    if find(town, a) == find(town, b):
        continue
    else:
        union(town, a, b)
        result = result + c
        max_c = c

print(result - max_c)

# 18분 28초 / Pass