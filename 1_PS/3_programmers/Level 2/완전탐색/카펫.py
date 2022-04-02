"""
Date    : 2022.03.30
Update  : 2022.04.03
Source  : 카펫.py
Purpose : 완전 탐색 / 약수
url     : https://programmers.co.kr/learn/courses/30/lessons/42842
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
def get_divisor(x):
    divisor = []
    for i in range(1, int(x ** 0.5 + 1)):
        if x % i == 0:
            divisor.append((x // i, i))

    return divisor


def check_edge(*args):
    return 2 * args[0][0] + 2 * args[0][1] - 4


def solution(brown, yellow):
    total = brown + yellow

    divisors = get_divisor(total)

    for i, edge in enumerate(map(check_edge, divisors)):
        if edge == brown:
            return divisors[i]

# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.10ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)
# 테스트 6 〉	통과 (0.44ms, 10.2MB)
# 테스트 7 〉	통과 (0.08ms, 10.2MB)
# 테스트 8 〉	통과 (0.07ms, 10.2MB)
# 테스트 9 〉	통과 (0.08ms, 10.3MB)
# 테스트 10 〉	통과 (0.07ms, 10.3MB)
# 테스트 11 〉	통과 (0.10ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10.3MB)
# 테스트 13 〉	통과 (0.02ms, 10.3MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0