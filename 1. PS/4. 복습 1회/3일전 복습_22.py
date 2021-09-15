# # 백준 - 10972 - 다음 순열
#
# n = int(input())
# array = list(map(int, input().split()))
#
# k = -1
#
# for i in range(len(array)-1):
#     if array[i] < array[i+1]:
#         k = i
#
# if k == -1:
#     print(-1)
# else:
#     m = 0
#     for j in range(k, len(array)):
#         if array[k] < array[j]:
#             m = j
#
#     array[k], array[m] = array[m], array[k]
#
#     temp = array[k+1:]
#     temp.sort()
#     answer = array[:k+1] + temp[:]
#
#     print(*answer, sep=' ')

# 6분 30초

# # 백준 - 10973 - 이전 순열
#
# n = int(input())
# array = list(map(int, input().split()))
#
# k = -1
#
# for i in range(len(array)-1):
#     if array[i] > array[i+1]:
#         k = i
#
# if k == -1:
#     print(-1)
# else:
#     m = 0
#
#     for j in range(k, len(array)):
#         if array[k] > array[j]:
#             m = j
#
#     array[k], array[m] = array[m], array[k]
#
#     temp = array[k+1:]
#     temp.sort(reverse=True)
#     answer = array[:k+1] + temp[:]
#
#     print(answer)

# 6분

# # 백준 - 1312 - 소수
#
# A, B, N = list(map(int, input().split()))
#
# A = A % B
# answer = 0
#
# for i in range(N):
#     A *= 10
#     answer = A // B
#     A = A % B
#
# print(answer)

# 5분분