# # 10972 - 다음 순열
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
#     for i in range(k, n):
#         if array[k] < array[i]:
#             m = i
#
#     array[k], array[m] = array[m], array[k]
#
#     temp = sorted(array[k+1:])
#     # print(temp)
#     answer = array[:k+1] + temp[:]
#
#     print(*answer, sep=' ')

# # 10973 - 이전 순열
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
#     for i in range(k, n):
#         if array[k] > array[i]:
#             m = i
#
#     array[k], array[m] = array[m], array[k]
#
#     temp = sorted(array[k+1:], reverse=True)
#
#     answer = array[:k+1] + temp[:]
#
#     print(*answer, sep=' ')

# 1312 - 소수

A, B, N = list(map(int, input().split()))

A = A % B

for i in range(N):
    A *= 10
    if i == N-1:
        Answer = A // B
    A %= B

print(Answer)