# # 괄호 변환
#
# def balance(p):
#     l_count = 0
#     r_count = 0
#
#     for i in range(len(p)):
#         if p[i] == '(':
#             l_count += 1
#         elif p[i] == ')':
#             r_count += 1
#
#         if l_count == r_count:
#             return i
#
#
# def right_str(u):
#     count = 0
#
#     for i in u:
#         if i == '(':
#             count += 1
#         elif i == ')':
#             count -= 1
#
#         if count < 0:
#             return False
#     return True
#
#
# def solution(p):
#     if len(p) == 0:
#         return ''
#
#     num = balance(p)
#
#     u = p[:num + 1]
#     v = p[num + 1:]
#
#     if right_str(u):
#         new = solution(v)
#         return u + new
#     elif not right_str(u):
#         new = '(' + solution(v) + ')'
#         u = u[1:-1]
#         new_u = ''
#         for i in u:
#             if i == '(':
#                 new_u += ')'
#             elif i == ')':
#                 new_u += '('
#         return new + new_u

# 연산자 끼워넣기

def recur(result, i, num_array, add, sub, mul, div, max_r, min_r):
    global n

    if n == i:
        max_r = max(max_r, result)
        min_r = min(min_r, result)
    else:
        if add != 0:
            max_r, min_r = recur(result + num_array[i], i+1, num_array, add-1, sub, mul, div, max_r, min_r)
        if sub != 0:
            max_r, min_r = recur(result - num_array[i], i+1, num_array, add, sub-1, mul, div, max_r, min_r)
        if mul != 0:
            max_r, min_r = recur(result * num_array[i], i+1, num_array, add, sub, mul-1, div, max_r, min_r)
        if div != 0:
            max_r, min_r = recur(int(result / num_array[i]), i+1, num_array, add, sub, mul, div-1, max_r, min_r)

    return max_r, min_r

n = int(input())
num_array = list(map(int, input().split()))
oper_array = list(map(int, input().split()))

max_r, min_r = recur(num_array[0], 1, num_array, oper_array[0], oper_array[1], oper_array[2], oper_array[3], -1e9, 1e9)

print(max_r)
print(min_r)