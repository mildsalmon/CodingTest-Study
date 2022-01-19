# n = int(input())
#
# tale = [(2,2),
#         (1,2),
#         (2,1)]
#
# array = []
# m = n // 2 + n % 2
# for i in range(m):
#     one = [0] * m
#     if i < n-1:
#         one[i] = 4
#     for j in range(len(one)):
#         if one[j] == 0:
#             one[j] = 1
#
#     array.append(one)
#
# print(array)
#
# # 실패 / 48분

n = int(input())

array = [0] * 1001

array[1] = 1
array[2] = 3

for i in range(3, n+1):
    array[i] = array[i-1] + array[i-2] * 2
    array[i] = array[i] % 796796

print(array[n])