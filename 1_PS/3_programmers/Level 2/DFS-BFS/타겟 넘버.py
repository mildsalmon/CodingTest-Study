"""
Date    : 2021.04.01
Update  : 2021.04.01
Source  : 타겟 넘버.py
Purpose : DFS
url     : https://programmers.co.kr/learn/courses/30/lessons/43165
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
from itertools import product


def solution(numbers, target):
    answer = 0
    temp = [[x, -x] for x in numbers]

    for num in product(*temp):
        if sum(num) == target:
            answer += 1

    return answer