"""
Date    : 2022.03.28
Update  : 2022.03.28
Source  : 소수 찾기.py
Purpose : dfs / 완전 탐색 / 재귀 / 소수
url     : https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
from itertools import permutations


def is_prime(x):
    if x <= 1:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    per = []

    for i in range(1, len(numbers) + 1):
        per.extend(list(permutations(numbers, i)))

    per = set(map(lambda x: int(''.join(x)), per))

    for value in per:
        if is_prime(value):
            answer += 1

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.06ms, 10.4MB)
# 테스트 2 〉	통과 (2.60ms, 10.4MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (1.17ms, 10.6MB)
# 테스트 5 〉	통과 (5.76ms, 11.4MB)
# 테스트 6 〉	통과 (0.04ms, 10.2MB)
# 테스트 7 〉	통과 (0.07ms, 10.4MB)
# 테스트 8 〉	통과 (5.29ms, 11.4MB)
# 테스트 9 〉	통과 (0.04ms, 10.2MB)
# 테스트 10 〉	통과 (5.48ms, 10.4MB)
# 테스트 11 〉	통과 (0.57ms, 10.3MB)
# 테스트 12 〉	통과 (0.21ms, 10.1MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0