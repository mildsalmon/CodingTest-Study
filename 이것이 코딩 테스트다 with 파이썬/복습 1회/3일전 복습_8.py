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

