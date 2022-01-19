"""
Date    : 2021.12.19
Update  : 2021.12.19
Source  : 11728.py
Purpose : 첫 방식과 비슷하게 다시 해봄.
url : https://www.acmicpc.net/problem/11728
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
n, m = list(map(int, input().split()))

# 두 배열은 정렬되어서 입력됨
A = list(map(int, input().split()))
B = list(map(int, input().split()))

"""
변경점
"""
answer = A + B
answer.sort()

print(*answer, sep=' ')
