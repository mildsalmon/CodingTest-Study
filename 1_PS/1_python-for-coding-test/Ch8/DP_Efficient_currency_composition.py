# n, m = list(map(int, input().split()))
# n_array = []
#
# array = [0] * 10001
#
# result = 0
#
# for i in range(n):
#     n_array.append(int(input()))
#
#
# for i in range(0, min(n_array)):
#     array[i] = 0
#
# # array[min(n_array)] = 1
#
# for i in range(min(n_array), m+1):
#     # print(array)
#     for j in range(len(n_array)):
#         if j+1 >= len(n_array):
#             continue
#         if i-n_array[j+1] < 0:
#             continue
#         array[i] = min(array[i-n_array[j]], array[i-n_array[j+1]]) + 1
# print(array)
# if array[min(n_array)] == 1:
#     result = array[m]
# else:
#     result = -1
#
# print(result)
#
# # 47분 / 실패

n, m = list(map(int, input().split()))
array = []
result = 0

for i in range(n):
    array.append(int(input()))

dp_table = [10001] * (m+1)

dp_table[0] = 0

for i in array:
    for j in range(i, m+1):
        dp_table[j] = min(dp_table[j], dp_table[j - i] + 1)

if dp_table[m] == 10001:
    result = -1
else:
    result = dp_table[m]

print(result)