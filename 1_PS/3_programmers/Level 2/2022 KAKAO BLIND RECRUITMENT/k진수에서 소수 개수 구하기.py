"""
Date    : 2022.02.14
Update  : 2022.02.14
Source  : k진수에서 소수 개수 구하기.py
Purpose : 수학 / 소수 / 진수 변환
url     : https://programmers.co.kr/learn/courses/30/lessons/92335
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import math


def is_prime(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def convert(n, k):
    binary = ''

    while n:
        binary = str(n % k) + binary
        n = n // k

    return binary

def solution(n, k):
    count = 0

    binary = convert(n, k)
    binary = binary.split('0')

    for num in binary:
        if num:
            if is_prime(int(num)):
                count += 1

    return count

# 채점을 시작합니다.
#
# 정확성  테스트
# 테스트 1 〉	통과 (89.66ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.4MB)
# 테스트 4 〉	통과 (0.02ms, 10.2MB)
# 테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.03ms, 10.2MB)
# 테스트 8 〉	통과 (0.03ms, 10.3MB)
# 테스트 9 〉	통과 (0.03ms, 10.3MB)
# 테스트 10 〉	통과 (0.03ms, 10.3MB)
# 테스트 11 〉	통과 (0.03ms, 10.3MB)
# 테스트 12 〉	통과 (0.02ms, 10.3MB)
# 테스트 13 〉	통과 (0.02ms, 10.3MB)
# 테스트 14 〉	통과 (0.02ms, 10.4MB)
# 테스트 15 〉	통과 (0.02ms, 10.4MB)
# 테스트 16 〉	통과 (0.02ms, 10.3MB)
#
# 채점 결과
#
# 정확성: 100.0
#
# 합계: 100.0 / 100.0