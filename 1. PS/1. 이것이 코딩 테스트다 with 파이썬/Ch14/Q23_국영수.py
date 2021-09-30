# n = int(input())
#
# array = []
#
# for _ in range(n):
#     temp = list(input().split())
#     array.append([temp[0], int(temp[1]), int(temp[2]), int(temp[3])])
#
# # 삽입 정렬
# for i in range(1, n):
#     for j in range(i, 0, -1):
#         # 국어 점수가 감수하는 순서로 -> 내림차순
#         if array[j][1] > array[j-1][1]:
#             array[j], array[j-1] = array[j-1], array[j]
#         # 국어 점수가 같을 경우
#         elif array[j][1] == array[j-1][1]:
#             # 영어 점수가 증가하는 순서로 -> 오름차순
#             if array[j][2] < array[j-1][2]:
#                 array[j], array[j - 1] = array[j - 1], array[j]
#             # 영어 점수가 같을 경우
#             elif array[j][2] == array[j-1][2]:
#                 # 수학 점수가 감수하는 순서로 -> 내림차순
#                 if array[j][3] > array[j-1][3]:
#                     array[j], array[j - 1] = array[j - 1], array[j]
#                 # 수학 점수가 같을 경우
#                 elif array[j][3] == array[j-1][3]:
#                     # 이름이 사전 순으로 증가하는 순서로 -> 오름차순
#                     if array[j][0] < array[j-1][0]:
#                         array[j], array[j - 1] = array[j - 1], array[j]
#
# for i in range(n):
#     print(array[i][0])
#
# # print(*array, sep='\n')

# 시간 초과

n = int(input())

array = []

for _ in range(n):
    temp = list(input().split())
    array.append([temp[0], int(temp[1]), int(temp[2]), int(temp[3])])

array.sort(key=lambda x: [-x[1], x[2], -x[3], x[0]])

for i in range(n):
    print(array[i][0])

# print(*array, sep='\n')