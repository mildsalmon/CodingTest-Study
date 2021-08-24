# Ch7_이진 탐색_부품 찾기

# 부품 N개 있다.
# 각 부품은 정수 형태의 고유 번호가 있다.
# 손님이 M개 종류의 부품을 구매하려한다.
# M개 종류를 모두 확인해서 견적서를 작성해야 한다.

# Input
# N (100만)
    # nlogn, n, logn
# 공백 구분하여 N개의 정수 (100만 이하)
# 정수 M (10만)
    # nlogn, n, logn
# 공백 구분하여 M개의 정수 (100만 이하)

# Ouput
# 각 부품이 존재하면 yes, 없으면 no

# n = int(input())
# A = list(map(int, input().split()))
# m = int(input())
# B = list(map(int, input().split()))
#
# A.sort()
#
# for i in B:
#     start = 0
#     end = len(A)-1 # n-1
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if i == A[mid]:
#             break
#         elif i < A[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     if i == A[mid]:
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')

# Ch5_DFS/BFS_음료수 얼려먹기

# NxM 크기의 얼음 틀
# 구멍 0 / 칸막이 1
# 구멍 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결된 것으로 간주.
# 총 아이스크림의 개수

# Input
# 1. 얼음 틀의 세로 길이 N, 가로 M (1000 이하)
# 2. N+1 줄까지 얼음 틀의 형태 주어짐
    # 구멍 0 / 구멍 x 1

# Output
# 한 번에 만들 수 있는 아이스크림 개수

from collections import deque

n, m = 15, 14
z =['00000111100000',
    '11111101111110',
    '11011101101110',
    '11011101100000',
    '11011111111111',
    '11011111111100',
    '11000000011111',
    '01111111111111',
    '00000000011111',
    '01111111111000',
    '00011111111000',
    '00000001111000',
    '11111111110011',
    '11100011111111',
    '11100011111111',]

# # n, m = list(map(int, input().split()))
# array = []
# que = deque()
# result = 0
# ds = ((-1, 0), (1, 0), (0, 1), (0, -1))
#
# for i in range(n):
#     array.append(list(map(int, z[i])))
# # print(array)
#
# def bfs(x, y, que):
#     # print(*array, sep='\n')
#     if array[x][y] == 1:
#         return 0
#
#     que.append([x, y])
#
#     while que:
#         nx, ny = que.popleft()
#         array[nx][ny] = 1
#
#         for i in ds:
#             dx = nx + i[0]
#             dy = ny + i[1]
#             # print(array[dx][dy])
#             if dx < 0 or dx >= n or dy < 0 or dy >= m:
#                 continue
#             if array[dx][dy] == 1:
#                 continue
#             else:
#                 que.append([dx, dy])
#     return 1
#
#
# for j in range(n):
#     for k in range(m):
#         result = result + bfs(j, k, que)
#
# print(result)

# 실수가 있어서, 38분 30초 걸림
# array를 입력받을 때, 정수처리를 안함.

# n, m = list(map(int, input().split()))
array = []
for i in range(n):
    array.append(list(map(int, z[i])))
result = 0

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    if array[x][y] == 1:
        return 0
    else:
        array[x][y] = 1

        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

        return 1

for i in range(n):
    for j in range(m):
        result = result + dfs(i, j)
print(result)

# 7분 35초