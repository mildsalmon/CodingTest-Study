# # 국영수
#
# n = int(input())
#
# array = []
#
# for i in range(n):
#     temp = list(input().split())
#
#     array.append([temp[0], int(temp[1]), int(temp[2]), int(temp[3])])
#
# array.sort(key=lambda x: [-x[1], x[2], -x[3], x[0]])
#
# for i in range(n):
#     print(array[i][0])

# 안테나

n = int(input())
array = list(map(int, input().split()))

# 3 -> 1
# 4 -> 1
# 5 -> 2
# 6 -> 2
array.sort()

array_len = len(array)

print(array[(array_len - 1) // 2])
