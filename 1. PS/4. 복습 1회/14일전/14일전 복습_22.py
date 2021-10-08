# # 다음 순열
#
# n = int(input())
# array = list(map(int, input().split()))
#
# k = -1
#
# for i in range(n-1):
#     if array[i] < array[i+1]:
#         k = i
#
# if k == -1:
#     print(-1)
# else:
#     for j in range(k, n):
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
#
# # 이전 순열
#
# n = int(input())
# array = list(map(int, input().split()))
#
# k = -1
#
# for i in range(n-1):
#     if array[i] > array[i+1]:
#         k = i
#
# if k == -1:
#     print(-1)
# else:
#     for j in range(k, n):
#         if array[k] > array[j]:
#             m = j
#
#     array[k], array[m] = array[m], array[k]
#
#     temp = array[k+1:]
#     temp.sort(reverse=True)
#
#     answer = array[:k+1] + temp[:]
#
#     print(*answer, sep=' ')

# 소수

A, B, N = list(map(int, input().split()))

A = A%B

for i in range(N):
    A *= 10
    answer = A // B
    A %= B

print(answer)