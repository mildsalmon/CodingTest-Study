"""
Date    : 2022.04.04
Update  : 2022.04.09
Source  : 가장 큰 수.py
Purpose : 정렬, 아이디어
url     : https://programmers.co.kr/learn/courses/30/lessons/42746
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    return str(int(''.join(numbers)))

print(solution([6, 10, 2, 0]))
print(solution([0, 0, 0]))
