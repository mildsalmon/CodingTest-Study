"""
Date    : 2021.12.06
Update  : 2021.12.06
Source  : 1182.py
Purpose : dfs 구현
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def dfs(arr, result, i, s):
    global count

    if i >= len(arr):
        return

    result += arr[i]

    if result == s:
        count += 1

    dfs(arr, result - arr[i], i+1, s)
    dfs(arr, result, i+1, s)

global count

n, s = list(map(int, input().split()))
array = list(map(int, input().split()))

result = 0
count = 0

dfs(array, result, 0, s)

print(count)

###############
# global 변수를 사용하지 않고 구현.


def dfs(arr, result, i, s):
    temp = 0

    if i >= len(arr):
        return 0

    result += arr[i]

    if result == s:
        temp += 1

    temp += dfs(arr, result - arr[i], i+1, s)
    temp += dfs(arr, result, i+1, s)

    return temp

n, s = list(map(int, input().split()))
array = list(map(int, input().split()))

result = 0
count = 0

count += dfs(array, result, 0, s)

print(count)
