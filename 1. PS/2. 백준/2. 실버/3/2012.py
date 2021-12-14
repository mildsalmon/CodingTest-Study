"""
Date    : 2021.12.14
Update  : 2021.12.14
Source  : 등수 매기기.py
Purpose : 계수정렬과 그리디를 이용하여 해결하였다.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
n = int(input())
array = []

for i in range(n):
    array.append(int(input()))

array.sort()
answer = 0

for i in range(1, n+1):
    if i != array[i-1]:
        answer += abs(array[i-1] - i)

print(answer)