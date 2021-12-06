"""
Date    : 2021.12.06
Update  : 2021.12.06
Source  : 10974.py
Purpose : 순열 구현
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
# 라이브러리 사용
# from itertools import permutations
#
# n = int(input())
#
# permu = list(permutations(range(1, n+1), n))
#
# for p in permu:
#     for a in p:
#         print(a, end=' ')
#     print()

def permutation(arr, visited, depth, r, result):
    n = len(arr)

    if r == depth:
        for i in range(n):
            print(result[i], end=' ')
        print()

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result.append(arr[i])
            permutation(arr, visited, depth+1, r, result)
            result.remove(arr[i])
            visited[i] = False

n = int(input())

visited = [False] * n
result = []

permutation(range(1, n+1), visited, 0, n, result)