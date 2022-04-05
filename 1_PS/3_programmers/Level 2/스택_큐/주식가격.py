"""
Date    : 2022.04.05
Update  : 2022.04.05
Source  : 주식가격.py
Purpose : stack / brute force
url     : https://programmers.co.kr/learn/courses/30/lessons/42584
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def solution(prices):
    answer = []

    for i in range(len(prices)):
        sec = 0
        for j, next_price in enumerate(prices[i + 1:]):
            sec += 1
            if prices[i] > next_price:
                break
        answer.append(sec)

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.06ms, 10.3MB)
# 테스트 3 〉	통과 (0.89ms, 10.2MB)
# 테스트 4 〉	통과 (1.12ms, 10.2MB)
# 테스트 5 〉	통과 (1.47ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.2MB)
# 테스트 7 〉	통과 (0.52ms, 10.2MB)
# 테스트 8 〉	통과 (0.66ms, 10.2MB)
# 테스트 9 〉	통과 (0.03ms, 10.3MB)
# 테스트 10 〉	통과 (1.54ms, 10.4MB)
#
# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)
#
# 채점 결과
# 정확성: 66.7
# 효율성: 0.0
# 합계: 66.7 / 100.0