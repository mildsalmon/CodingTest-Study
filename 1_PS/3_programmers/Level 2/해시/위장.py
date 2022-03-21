"""
Date    : 2021.12.17
Update  : 2021.03.21
Source  : 위장.py
Purpose : 경우의 수 계산
url     : https://programmers.co.kr/learn/courses/30/lessons/42578
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from functools import reduce
from collections import Counter


def solution(clothes):
    kind_by_cnt = Counter(list(map(lambda x: x[1], clothes)))
    answer = reduce(lambda y, x: y * (x + 1), kind_by_cnt.values(), 1) - 1

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.1MB)
# 테스트 4 〉	통과 (0.03ms, 10.1MB)
# 테스트 5 〉	통과 (0.04ms, 10.1MB)
# 테스트 6 〉	통과 (0.02ms, 10.3MB)
# 테스트 7 〉	통과 (0.04ms, 10.1MB)
# 테스트 8 〉	통과 (0.03ms, 10.1MB)
# 테스트 9 〉	통과 (0.02ms, 10.1MB)
# 테스트 10 〉	통과 (0.03ms, 10.2MB)
# 테스트 11 〉	통과 (0.03ms, 10.1MB)
# 테스트 12 〉	통과 (0.03ms, 10.2MB)
# 테스트 13 〉	통과 (0.03ms, 10.2MB)
# 테스트 14 〉	통과 (0.02ms, 10.1MB)
# 테스트 15 〉	통과 (0.03ms, 10.1MB)
# 테스트 16 〉	통과 (0.02ms, 9.87MB)
# 테스트 17 〉	통과 (0.03ms, 10.2MB)
# 테스트 18 〉	통과 (0.03ms, 10.1MB)
# 테스트 19 〉	통과 (0.03ms, 10.1MB)
# 테스트 20 〉	통과 (0.03ms, 10.1MB)
# 테스트 21 〉	통과 (0.02ms, 10.2MB)
# 테스트 22 〉	통과 (0.03ms, 10.3MB)
# 테스트 23 〉	통과 (0.02ms, 10.1MB)
# 테스트 24 〉	통과 (0.02ms, 10MB)
# 테스트 25 〉	통과 (0.03ms, 10.1MB)
# 테스트 26 〉	통과 (0.03ms, 10.1MB)
# 테스트 27 〉	통과 (0.03ms, 10.1MB)
# 테스트 28 〉	통과 (0.03ms, 10.2MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0