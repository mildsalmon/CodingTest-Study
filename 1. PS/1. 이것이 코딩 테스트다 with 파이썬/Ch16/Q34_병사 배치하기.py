# n = int(input())
# array = list(map(int, input().split()))
# dp = [-1] * n
#
# for i in range(n):
#     count = 0
#     for j in range(i, n):
#         if array[i] > array[j]:
#             count += 1
#     if count == n - i - 1:
#         dp[i] = array[i]
# # print(dp)
# count = 0
# for d in dp:
#     if d == -1:
#         count += 1
#
# print(count)

####################################################

n = int(input())
array = list(map(int, input().split()))
dp = [array[-1]]

for i in range(n-2, -1, -1):
    if dp[-1] < array[i]:
        dp.append(array[i])

print(n - len(dp))

n = int(input())
array = list(map(int, input().split()))
dp = [1] * n

array = array[::-1]

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)
            # print(i, "|", dp)

print(n - max(dp))