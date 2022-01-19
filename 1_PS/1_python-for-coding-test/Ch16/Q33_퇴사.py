# n = int(input())
# array = []
#
# for i in range(n):
#     temp = list(map(int, input().split()))
#
#     array.append(temp)
#
# # array.append([0, 0])
#
# dp = [0] * (n+1)
#
# for i in range(n):
#     t, p = array[i]
#     # temp = array[t+i][0]
#     # j = [i]
#     save_day = []
#     if i + t <= n:
#         temp = i
#
#         while temp + array[temp][0] < n:
#             save_day.append(temp)
#             temp += array[temp][0]
#
#     # print(j)
#     for a in save_day:
#         dp[i] += array[a][1]
#
# print(max(dp))

## 오른쪽으로 가는건 안됨.

# n = int(input())
# array = []
#
# for i in range(n):
#     temp = list(map(int, input().split()))
#
#     array.append(temp)
#
# # array.append([0, 0])
#
# dp = [0] * (n+1)
#
# for i in range(n):
#     next_day = i + array[i][0]
#
#     if next_day < n:
#         dp[next_day] = max(dp[i] + array[next_day][1], dp[next_day]) + array[i][1]
#
# print(max(dp))

#########################################

# n = int(input())
# array = []
#
# for i in range(n):
#     temp = list(map(int, input().split()))
#
#     array.append(temp)
#
# # array.append([0, 0])
#
# dp = [0] * (n+1)
#
# for i in range(n-1, -1, -1):
#     next_day = array[i][0] + i
#     answer = max(dp)
#
#     if next_day <= n:
#         dp[i] = max(dp[next_day] + array[i][1], answer)
#     else:
#         dp[i] = answer
#
# answer = max(dp)
#
# print(answer)

################################

# n = int(input())
# array = []
#
# for i in range(n):
#     temp = list(map(int, input().split()))
#
#     array.append(temp)
#
# # array.append([0, 0])
#
# dp = [0] * (n + 1)
#
# for i in range(n - 1, -1, -1):
#     next_day = array[i][0] + i
#
#     if next_day <= n:
#         dp[i] = max(dp[next_day] + array[i][1], max(dp))
#     else:
#         dp[i] = max(dp)
#
# print(max(dp))
#
# #################################
#
# n = int(input())
# array = []
#
# for i in range(n):
#     temp = list(map(int, input().split()))
#
#     array.append(temp)
#
# # array.append([0, 0])
#
# dp = [0] * (n+1)
# answer = 0
#
# for i in range(n-1, -1, -1):
#     next_day = array[i][0] + i
#
#     if next_day <= n:
#         dp[i] = max(dp[next_day] + array[i][1], answer)
#         answer = dp[i]
#     else:
#         dp[i] = answer
#
# print(max(dp))

######################################

n = int(input())
array = []

for i in range(n):
    temp = list(map(int, input().split()))

    array.append(temp)

# array.append([0, 0])

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    next_day = array[i][0] + i

    if next_day <= n:
        dp[i] = max(dp[next_day:]) + array[i][1]

print(max(dp))