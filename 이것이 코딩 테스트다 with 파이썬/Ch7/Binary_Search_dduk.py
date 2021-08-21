# n, m = list(map(int, input().split()))
# array = list(map(int, input().split()))
#
# array.sort(reverse=True)
#
# m2 = 0
#
# while(m > m2):
#     max_value = max(array)
#     for i in range(len(array)):
#         if array[i] == max_value:
#             array[i] = array[i] - 1
#             m2 = m2 + 1
#     # print("array : ", array)
#     # print("m2 : ", m2)
#
# result = max(array)
#
# print(result)
#
# # 내가 만든 테스트 케이스
# # 4 10
# # 1 21 20 3

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

while (start <= end):
    mid = (start + end) // 2
    dduk_len = 0
    for i in array:
        if i > mid:
            dduk_len = dduk_len + (i - mid)
    if dduk_len > m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)