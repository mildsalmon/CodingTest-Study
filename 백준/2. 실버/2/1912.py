n = int(input())
array = list(map(int, input().split()))
answer = -1001

# for i in range(len(array)):
#     for j in range(0, len(array)):#, i+1):
#         start = j
#         end = j + i+1
#         answer.append(sum(array[start:end]))
#         # print(answer)
#
# print(max(answer))

# A = sorted(array, reverse=True)
# B = []
# # print(A)
# for i in A:
#     B.append(array.index(i))
#
# # print(B)
# big = B[0]
# start = 0
# end = len(B)-1
# for i in range(len(B)):
#     if B[i] <= B[0]:
#         answer = max(answer, (sum(array[B[i]:B[0]+1])))
#         start = i
#     else:
#         answer = max(answer, (sum(array[B[0]:B[i]+1])))
#         end = i
#     answer = max(answer, sum(array[B[start]:B[end]+1]))
#
# print(answer)

# answer = sum(array)
#
# for i in range(len(array)-1):
#     if array[0] >= array[-1]:
#         array.pop()
#     elif array[0] < array[-1]:
#         array.pop(0)
#     answer = max(answer, sum(array))
#
# print(answer)
#
answer = []
answer.append(array[0])
for i in range(1, n):
    answer.append(max(answer[i-1]+array[i], array[i]))

print(max(answer))