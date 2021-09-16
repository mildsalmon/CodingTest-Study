# # Ch12_구현_럭키 스트레이트
#
# # 공백이 없으면, input() / 공백이 있으면 input().split()
# array = list(map(int, input()))
# len_array = len(array)
# left_sum = 0
# right_sum = 0
#
# for i in range(len_array):
#     if i < (len_array//2):
#         left_sum += array[i]
#     elif i >= (len_array//2):
#         right_sum += array[i]
#
# if left_sum == right_sum:
#     print("LUCKY")
# else:
#     print("READY")

# 5분 30초

# Ch12_구현_문자열 재정렬

array = input()
answer = []
sum = 0

for a in array:
    if a.isalpha():
        answer.append(a)
    else:
        sum += int(a)

answer.sort()

print(''.join(answer)+str(sum))

# 2분 20초