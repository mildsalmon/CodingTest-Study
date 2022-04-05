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
        for j, next_price in enumerate(prices[i + 1:]):
            sec += 1
            if price > next_price:
                break
        answer.append(sec)

    return answer

solution([1,2,3,2,3])

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.06ms, 10.2MB)
# 테스트 3 〉	통과 (0.84ms, 10.4MB)
# 테스트 4 〉	통과 (1.04ms, 10.4MB)
# 테스트 5 〉	통과 (1.36ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.48ms, 10.2MB)
# 테스트 8 〉	통과 (0.60ms, 10.3MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)
# 테스트 10 〉	통과 (1.45ms, 10.4MB)
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