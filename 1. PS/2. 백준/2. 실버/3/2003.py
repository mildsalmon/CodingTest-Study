n, m = list(map(int, input().split()))
array = list(map(int, input().split()))
count = 0

# for i in range(n):
#     for j in range(i+1, n+1):
#         temp = sum(array[i:j])
#         if temp == m:
#             count += 1
#         elif temp > m:
#             break
#         else:
#             continue
#
# print(count)

# 시간초과
# O(N^2)

# sum_array = [0] * (n+1)
# sum_array[0] = array[0]
# sum_array[1] = array[1] + sum_array[0]
#
# for i in range(2, n):
#     sum_array[i] = array[i] + sum_array[i-1]
#
# for i in range(n):
#     if sum_array[i] == m:
#         count += 1
#         continue
#     temp = 0
#     for j in range(0, i):
#         temp += array[j]
#
#         if sum_array[i] - temp == m:
#             count += 1
#         elif sum_array[i] - temp < m:
#             break
#         else:
#             continue
#
# print(count)

# 인덱스 에러

temp = 0
l_p, r_p = 0, 1

while True:
    temp = sum(array[l_p:r_p])

    if temp < m:
        r_p += 1
    elif temp > m:
        l_p += 1
    elif temp == m:
        count += 1
        r_p += 1
        l_p += 1
    if r_p > len(array) or l_p > len(array):
        break

print(count)

# 투포인터