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

    for i, price in enumerate(prices):
        sec = 0
        for j in range(i + 1, len(prices)):
            sec += 1
            if price > prices[j]:
                break
        answer.append(sec)

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.05ms, 10.2MB)
# 테스트 3 〉	통과 (0.51ms, 10.4MB)
# 테스트 4 〉	통과 (0.56ms, 10.4MB)
# 테스트 5 〉	통과 (0.73ms, 10.4MB)
# 테스트 6 〉	통과 (0.02ms, 10.1MB)
# 테스트 7 〉	통과 (0.33ms, 10.2MB)
# 테스트 8 〉	통과 (0.39ms, 10.2MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)
# 테스트 10 〉	통과 (0.72ms, 10.4MB)
#
# 효율성  테스트
# 테스트 1 〉	통과 (107.82ms, 18.9MB)
# 테스트 2 〉	통과 (81.62ms, 17.6MB)
# 테스트 3 〉	통과 (132.60ms, 19.4MB)
# 테스트 4 〉	통과 (93.62ms, 18MB)
# 테스트 5 〉	통과 (63.30ms, 16.7MB)
#
# 채점 결과
# 정확성: 66.7
# 효율성: 33.3
# 합계: 100.0 / 100.0