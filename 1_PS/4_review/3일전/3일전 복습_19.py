# # Ch11_그리디_곱하기 혹은 더하기
#
# s = input()
# answer = 0
# for i in s:
#     i = int(i)
#     # print((i))
#     if i == 0 or i == 1:
#         answer += i
#     else:
#         if answer == 0:
#             answer += i
#         else:
#             answer *= i
#
# print(answer)

# Ch11_그리디_문자열 뒤집기

s = input()

first = s[0]
pre = s[0]
count = 0

for i in range(1, len(s)):
    if s[i] != first and s[i] != pre:
        count += 1
        pre = s[i]
print(count)