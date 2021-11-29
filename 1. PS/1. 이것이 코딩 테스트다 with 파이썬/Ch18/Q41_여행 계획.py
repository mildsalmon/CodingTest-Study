"""
Date    : 2021.11.26
Update  : 2021.11.26
Source  : Q41_여행 계획.py
Purpose : union-find 알고리즘으로 여행 계획이 가능한지를 판단한다.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
# 부모노드 찾기
def find_parent(array, x):
    if array[x] != x:
        array[x] = find_parent(array, array[x])
    return array[x]

# 부모노드 합치기
def union_parent(array, a, b):
    a = find_parent(array, a)
    b = find_parent(array, b)

    if a > b:
        array[a] = b
    elif b > a:
        array[b] = a

# 여행 계획이 가능한지 확인
def check_plan(plan, parent):
    save_point = find_parent(parent, plan[0])

    for i in range(1, len(plan)):
        if find_parent(parent, i) != save_point:
            return "NO"
    return "YES"

# n = 여행지의 수, m = 여행 계획에 속한 도시의 수
n, m = list(map(int, input().split()))
graph = [[] for i in range(n)]

# 부모 노드
parent = [i for i in range(n)]

for i in range(n):
    temp = list(map(int, input().split()))

    # A지역에서 B지역으로 갈 수 있는 경우를 인접리스트 형식으로 저장
    for j in range(len(temp)):
        if temp[j] == 1:
            graph[i].append(j)

# 인접리스트를 순차적으로 접근하면서, 부모 노드가 다르다면, union
for i in range(len(graph)):
    for j in graph[i]:
        if find_parent(parent, j) != find_parent(parent, i):
            union_parent(parent, i, j)

plan = list(map(int, input().split()))

print(check_plan(plan, parent))
