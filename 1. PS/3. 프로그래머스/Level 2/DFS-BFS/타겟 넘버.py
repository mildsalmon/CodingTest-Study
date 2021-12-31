"""
Date    : 2021.12.31
Update  : 2021.12.31
Source  : 타겟 넘버.py
Purpose : DFS
url     : https://programmers.co.kr/learn/courses/30/lessons/43165
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from itertools import product

def solution(numbers, target) -> int:
    iter: list = [(x, -x) for x in numbers]
    # product는 db의 cartesian product이다.
    # 따라서, iter의 모든 원소의 데카르트 곱이 반환된다.
        # [(1, -1), (2, -2)] 이면, (1, 2), (1, -2), (-1, 2), (-1, -2)이다.
    answer: list = list(map(sum, product(*iter)))

    return answer.count(target)

if __name__ == "__main__":
    print(solution([1,1,2,2,1], 3))
