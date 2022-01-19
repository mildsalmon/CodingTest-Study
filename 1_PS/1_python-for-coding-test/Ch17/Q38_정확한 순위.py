"""
Date    : 2021.11.24
Update  : 2021.11.24
Source  : Q38_정확한 순위.py
Purpose : 플로이드 알고리즘을 사용하여 학생들의 성적 순위를 알 수 있는 경우를 구함
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
# n = 학생들의 수
# m = 성적을 비교한 횟수
n, m = list(map(int, input().split()))
# 학생들의 성적 비교가 가능한 경우의 인접행렬
array = [[1e9]*(n+1) for i in range(n+1)]

# 초기 비교 횟수 입력
for i in range(m):
    A, B = list(map(int, input().split()))

    array[A][B] = 1

# 자기 자신과 비교하는 경우는 0으로 입력
for i in range(n+1):
    array[i][i] = 0

# i -> k -> j가 i -> j보다 작다면 값을 교체
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            array[i][j] = min(array[i][k] + array[k][j], array[i][j])

# print(*array, sep='\n')

result = 0

# A -> B인 경우와 B -> A인 경우 중 최단 거리를 구했다면, count를 증가시킴.
# count가 학생수와 같다면 결과값을 증가시킴.
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if array[i][j] != 1e9 or array[j][i] != 1e9:
            count += 1
    if count == n:
        result += 1
print(result)

############
#### 플로이드로 안풀려서 다익스트라로 풀려고 했는데, cost 처리를 못함.
############

# from collections import deque
#
# n, m = list(map(int, input().split()))
#
# array = [[] for i in range(n+1)]
#
# distance = [0] * (n+1)
# q = deque()
#
# for i in range(m):
#     A, B = list(map(int, input().split()))
#
#     array[A].append(B)
#
# for i in range(n):
#     q.append(i)
#
# while q:
#     x = q.popleft()
#
#     for i in range(array[x]):
#         distance[x] += 1
#         distance[i] += distance[x]