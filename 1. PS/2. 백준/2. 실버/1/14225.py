"""
Date    : 2021.12.09
Update  : 2021.12.09
Source  : 14225.py
Purpose : dfs를 이용하여 구현하는 문제
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def dfs(answer, array, depth, partial_sum):
    if depth >= len(array):
        return

    partial_sum += array[depth]
    answer.append(partial_sum)

    dfs(answer, array, depth+1, partial_sum-array[depth])
    # if partial_sum in answer:
    #     return
    dfs(answer, array, depth+1, partial_sum)

def check(answer):
    for i in range(1, max(answer) + 1):
        if i not in answer:
            return i
    return max(answer)+1

n = int(input())
array = list(map(int, input().split()))

answer = []
# array.sort()
dfs(answer, array, 0, 0)
# print(answer)

print(check(answer))