"""
Date    : 2022.04.04
Update  : 2022.04.04
Source  : 가장 큰 수.py
Purpose : 정렬, 아이디어
url     : https://programmers.co.kr/learn/courses/30/lessons/42746
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def solution(numbers):
    zeros = [number for number in numbers if number % 10 == 0]
    others = [number for number in numbers if number % 10]

    others = list(map(str, others))
    zeros = list(map(str, zeros))

    others.sort(reverse=True)

    answer = ''.join(others)

    zero_sort = [[], [], [], []]
    for zero in zeros:
        if zero == 0:
            zero_sort[3].append(zero)
        elif zero % 1000 == 0:
            zero_sort[2].append(zero)
        elif zero % 100 == 0:
            zero_sort[1].append(zero)
        elif zero % 10 == 0:
            zero_sort[0].append(zero)

    for i in range(4):
        if zero_sort[i]:
            zero_sort[i].sort(reverse=True)
            answer += ''.join(map(str, zero_sort[i]))

    return answer

solution([6, 10, 2])
