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
    dfs(answer, array, depth+1, partial_sum)

def check(answer):
    # set으로 강제형변환을 for문 안에서 반복해주면 시간복잡도가 오래걸린다.
    # 대충 생각했을때는 얼마 안걸리겠지 싶었는데, 이것때문에 시간초과가 발생했다.
    max_value = max(answer)
    answer = set(answer)
    for i in range(1, max_value+1):
        if i not in answer:
            return i
    return max_value+1

n = int(input())
array = list(map(int, input().split()))

answer = []
# array.sort()
dfs(answer, array, 0, 0)
# print(answer)

print(check(answer))