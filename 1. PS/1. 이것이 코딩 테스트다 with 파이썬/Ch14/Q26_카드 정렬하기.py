# n = int(input())
#
# array = []
#
# for i in range(n):
#     array.append(int(input()))
#
# array.sort()
# answer = array[0] + array[1]
#
# for i in range(2, n):
#     answer = 2 * answer + array[i]
#     array.append(answer)
#     array.sort()
#
# print(answer)

import heapq

n = int(input())

array = []

for i in range(n):
    temp = int(input())

    heapq.heappush(array, temp)

sum_a = 0

while array:
    if len(array) == 1:
        # sum_a += heapq.heappop(array)
        break
    else:
        x = heapq.heappop(array)
        y = heapq.heappop(array)

        result = x + y
        sum_a += result
        heapq.heappush(array, result)

print(sum_a)