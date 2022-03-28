"""
Date    : 2022.03.28
Update  : 2022.03.28
Source  : 소수 찾기.py
Purpose : dfs / 완전 탐색 / 재귀 / 소수
url     : https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import math


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def make_number(depth, numbers, visited, result):
    global nums

    if depth == len(numbers):
        nums.add(int(result))
        return

    for i in range(len(numbers)):
        if visited[i]:
            make_number(depth + 1, numbers, visited[:], result)
            continue
        visited[i] = True
        make_number(depth + 1, numbers, visited[:], result + numbers[i])
        visited[i] = False


def solution(numbers):
    global nums

    answer = 0
    nums = set()

    visited = [False for _ in range(len(numbers))]
    make_number(0, numbers, visited, '')

    for num in nums:
        if is_prime(num):
            answer += 1

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.18ms, 10.4MB)
# 테스트 2 〉	통과 (23.39ms, 10.5MB)
# 테스트 3 〉	통과 (0.03ms, 10.5MB)
# 테스트 4 〉	통과 (21.60ms, 10.4MB)
# 테스트 5 〉	통과 (373.27ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.4MB)
# 테스트 7 〉	통과 (0.19ms, 10.4MB)
# 테스트 8 〉	통과 (367.91ms, 10.5MB)
# 테스트 9 〉	통과 (0.05ms, 10.3MB)
# 테스트 10 〉	통과 (26.90ms, 10.4MB)
# 테스트 11 〉	통과 (2.57ms, 10.4MB)
# 테스트 12 〉	통과 (1.67ms, 10.4MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0