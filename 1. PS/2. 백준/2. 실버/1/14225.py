"""
Date    : 2021.12.09
Update  : 2021.12.09
Source  : 14225.py
Purpose : dfs를 이용하여 구현하는 문제
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

n = int(input())
array = list(map(int, input().split()))
array.sort()

num = 1

for i in array:
    if num < i:
        break
    num += i

print(num)