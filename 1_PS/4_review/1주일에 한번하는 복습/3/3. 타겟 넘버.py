"""
Date    : 2022.01.01
Update  : 2022.01.01
Source  : 타겟 넘버.py
Purpose : cartesian product
url     : https://programmers.co.kr/learn/courses/30/lessons/43165
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from itertools import product


def solution(numbers, target):
    case = [(x, -x) for x in numbers]

    target_numbers = list(map(sum, product(*case)))

    return target_numbers.count(target)