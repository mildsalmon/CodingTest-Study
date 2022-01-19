# # 괄호 변환
#
# def balance_str(w):
#     l_count = 0
#     r_count = 0
#
#     for i in w:
#         if i == '(':
#             l_count += 1
#         elif i == ')':
#             r_count += 1
#
#         if l_count == r_count:
#             return l_count + r_count
#
# def right_str(u):
#     count = 0
#
#     if u[0] == '(':
#         for i in u:
#             if i == '(':
#                 count += 1
#             elif i == ')':
#                 count -= 1
#
#             if count < 0:
#                 return False
#         return True
#     elif u[0] == ')':
#         return False
#
#
# def solution(p):
#     if len(p) == 0:
#         return p
#
#     split_num = balance_str(p)
#
#     u = p[:split_num]
#     v = p[split_num:]
#
#     # print(u)
#
#     if right_str(u) == True:
#         # temp = solution(v)
#         # if len(temp)
#         answer = u + solution(v)
#         return answer
#     elif right_str(u) == False:
#         answer = '(' + solution(v) + ')'
#         u = u[1:-1]
#         for i in u:
#             if i == '(':
#                 answer += ')'
#             elif i == ')':
#                 answer += '('
#
#         return answer
#
# print(solution("()))((()"))
#
# # 23분 / pass
#

# 연산자 끼워넣기

def recursive(result, depth, add, sub, mul, div, max_answer, min_answer):
    global N, array

    if depth == N:
        max_answer = max(result, max_answer)
        min_answer = min(result, min_answer)

    elif depth != N:
        if add > 0:
            max_answer, min_answer = recursive(result + array[depth], depth+1, add-1, sub, mul, div, max_answer, min_answer)
        if sub > 0:
            max_answer, min_answer = recursive(result - array[depth], depth+1, add, sub-1, mul, div, max_answer, min_answer)
        if mul > 0:
            max_answer, min_answer = recursive(result * array[depth], depth+1, add, sub, mul-1, div, max_answer, min_answer)
        if div > 0:
            max_answer, min_answer = recursive(int(result / array[depth]), depth+1, add, sub, mul, div-1, max_answer, min_answer)

    return max_answer, min_answer
global N, array

N = int(input())
array = list(map(int, input().split()))
oper = list(map(int, input().split()))

max_answer = -1e9
min_answer = 1e9

max_answer, min_answer = recursive(array[0], 1, oper[0], oper[1], oper[2], oper[3], max_answer, min_answer)

print(max_answer)
print(min_answer)