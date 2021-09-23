# permutation - list

# from itertools import permutations
#
# n = int(input())
#
# array = list(map(int, input().split()))
# oper = list(map(int, input().split()))
# op = ['+', '-', '*', '/']
# oper_list = []
#
# for i in range(len(oper)):
#     for j in range(oper[i]):
#         oper_list.append(op[i])
#
# # print(oper_list)
#
# combi_oper = list(permutations(oper_list, n-1))
#
# # print(*combi_oper, sep='\n')
#
# max_answer = -1e9
# min_answer = 1e9
# for i in combi_oper:
#     answer = array[0]
#     for j in range(1, n):
#         if i[j-1] == "+":
#             answer = answer + array[j]
#         if i[j-1] == "*":
#             answer = answer * array[j]
#         if i[j-1] == "-":
#             answer = answer - array[j]
#         if i[j-1] == "/":
#             if answer < 0:
#                 answer = ((answer * -1) // array[j]) * -1
#             elif answer > 0:
#                 answer = int(answer // array[j])
#             else:
#                 pass
#         # print(i[j-1])
#     # print(i)
#     # if max_answer == 0 or min_answer == 1e9:
#     #     max_answer = answer
#     #     min_answer = answer
#
#     max_answer = max(answer, max_answer)
#     min_answer = min(answer, min_answer)
#
# print(max_answer)
# print(min_answer)
#

# permutation - set

# from itertools import permutations
#
# n = int(input())
#
# array = list(map(int, input().split()))
# oper = list(map(int, input().split()))
# op = ['+', '-', '*', '/']
# oper_list = []
#
# for i in range(len(oper)):
#     for j in range(oper[i]):
#         oper_list.append(op[i])
#
# # print(oper_list)
#
# combi_oper = set(permutations(oper_list, n-1))
#
# # print(*combi_oper, sep='\n')
#
# max_answer = -1e9
# min_answer = 1e9
# for i in combi_oper:
#     answer = array[0]
#     for j in range(1, n):
#         if i[j-1] == "+":
#             answer = answer + array[j]
#         if i[j-1] == "*":
#             answer = answer * array[j]
#         if i[j-1] == "-":
#             answer = answer - array[j]
#         if i[j-1] == "/":
#             if answer < 0:
#                 answer = ((answer * -1) // array[j]) * -1
#             elif answer > 0:
#                 answer = int(answer // array[j])
#             else:
#                 pass
#         # print(i[j-1])
#     # print(i)
#     # if max_answer == 0 or min_answer == 1e9:
#     #     max_answer = answer
#     #     min_answer = answer
#
#     max_answer = max(answer, max_answer)
#     min_answer = min(answer, min_answer)
#
# print(max_answer)
# print(min_answer)

# # 재귀
# # 더 빠른 이유는 이전에 계산했던 값을 다시 계산하지 않기 때문.
#
# def recursive(total, oper, i):
#     global max_answer, min_answer, array, n
#
#     # 두 코드(if문)는 같은
#     # if sum(oper) == 0:
#     if i == n:
#         max_answer = max(max_answer, total)
#         min_answer = min(min_answer, total)
#         return
#     else:
#         if oper[0] != 0:
#             oper[0] -= 1
#             recursive(total + array[i], oper, i+1)
#             oper[0] += 1
#         if oper[1] != 0:
#             oper[1] -= 1
#             recursive(total - array[i], oper, i+1)
#             oper[1] += 1
#         if oper[2] != 0:
#             oper[2] -= 1
#             recursive(total * array[i], oper, i+1)
#             oper[2] += 1
#         if oper[3] != 0:
#             oper[3] -= 1
#             recursive(int(total / array[i]), oper, i+1)
#             oper[3] += 1
#
#
# global max_answer, min_answer, array, n
#
# n = int(input())
# array = list(map(int, input().split()))
# oper = list(map(int, input().split()))
#
# max_answer = -1e9
# min_answer = 1e9
#
# recursive(array[0], oper, 1)
#
# print(max_answer)
# print(min_answer)

# 재귀
# 더 빠른 이유는 이전에 계산했던 값을 다시 계산하지 않기 때문.
# 좀 더 간결한 코드 / 이렇게도 하는구나.

def recursive(total, i, add, sub, mul, div):
    global max_answer, min_answer, array, n

    # 두 코드(if문)는 같은
    # if sum(oper) == 0:
    if i == n:
        max_answer = max(max_answer, total)
        min_answer = min(min_answer, total)
        return
    else:
        if add != 0:
            recursive(total + array[i], i+1, add-1, sub, mul, div)
        if sub != 0:
            recursive(total - array[i], i+1, add, sub-1, mul, div)
        if mul != 0:
            recursive(total * array[i], i+1, add, sub, mul-1, div)
        if div != 0:
            recursive(int(total / array[i]), i+1, add, sub, mul, div-1)


global max_answer, min_answer, array, n

n = int(input())
array = list(map(int, input().split()))
oper = list(map(int, input().split()))

max_answer = -1e9
min_answer = 1e9

recursive(array[0], 1, oper[0], oper[1], oper[2], oper[3])

print(max_answer)
print(min_answer)