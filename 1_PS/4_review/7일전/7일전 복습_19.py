# # Ch11_그리디_Q2. 곱하기 혹은 더하기
#
# s = input()
# answer = 0
# for i in s:
#     if int(i) <= 1 or answer == 0:
#         answer += int(i)
#     else:
#         answer *= int(i)
#
# print(answer)
#
# # 3분 24초
#
# # Ch11_그리디_문자열 뒤집기기
#
# s = input()
#
# first = s[0]
# pre = s[0]
# count = 0
#
# for i in s:
#     if i != first and i != pre:
#         count += 1
#     pre = i
#
# print(count)
#
# # 3분 30초