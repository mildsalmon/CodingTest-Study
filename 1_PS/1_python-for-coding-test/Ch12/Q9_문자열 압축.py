def solution(s):
    # pre = s[0]
    best_len = len(s)

    for i in range(1, len(s)):
        pre = s[:i]
        count = 0
        answer = ''
        for j in range(0, len(s)+i, i):
            now = s[j:j + i]
            # print("now : ", now)
            # print("pre : ", pre)
            if pre == now:
                count += 1
            else:
                # print(count)
                if count > 1:
                    answer = answer + str(count) + pre
                else:
                    answer = answer + pre
                pre = now
                count = 1
        # if count > 1:
        #     answer = answer + str(count) + pre
        # else:
        #     answer = answer + pre
        # print(answer)
        if best_len > len(answer):
            best_len = len(answer)
        # print(best_len)
    return best_len

print(solution("aabbaccc"))

# ## 나동빈님 코드
#
# def solution(s):
#     # pre = s[0]
#     best_len = len(s)
#
#     for i in range(1, len(s)// 2+1):
#         pre = s[:i]
#         count = 1
#         answer = ''
#         for j in range(i, len(s), i):
#             now = s[j:j + i]
#             # print("now : ", now)
#             # print("pre : ", pre)
#             if pre == now:
#                 count += 1
#             else:
#                 # print(count)
#                 if count > 1:
#                     answer = answer + str(count) + pre
#                 else:
#                     answer = answer + pre
#                 pre = now
#                 count = 1
#         if count > 1:
#             answer = answer + str(count) + pre
#         else:
#             answer = answer + pre
#         # print(answer)
#         best_len = min(best_len, len(answer))
#     return best_len
#
# print(solution("aabbaccc"))