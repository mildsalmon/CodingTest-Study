"""
Date    : 2021.12.07
Update  : 2021.12.07
Source  : 3273.py
Purpose : 정렬 후 양쪽 끝에서 다가오는 투포인터 문제
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

n = int(input())
array = list(map(int, input().split()))
result = int(input())

p1 = 0
p2 = n-1

array.sort()
count = 0

while True:
    if p1 == p2:
        break
    sum_num = array[p1] + array[p2]

    if sum_num > result:
        p2 -= 1
    elif sum_num < result:
        p1 += 1
    else:
        count += 1
        p2 -= 1

print(count)