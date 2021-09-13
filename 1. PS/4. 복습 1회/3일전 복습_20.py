# # Ch11_그리디_만들 수 없는 금액
#
# n = int(input())
# array = list(map(int, input().split()))
#
# array.sort()
# result = 1
# answer = 0
# for i in range(n):
#     if result >= array[i]:
#         result += array[i]
#     else:
#         answer = result
#
# print(answer)

# 26분 / Pass

# # Ch11_그리디_볼링공 고르기
#
# from itertools import combinations
#
# n, m = list(map(int, input().split()))
# array = list(map(int, input().split()))
#
# All_combi = combinations(array, 2)
# count = 0
#
# for i in All_combi:
#     if i[0] != i[1]:
#         count += 1
#
# print(count)

# 10분