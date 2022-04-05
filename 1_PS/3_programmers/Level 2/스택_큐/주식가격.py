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
        for j in prices[i + 1:]:
            sec += 1
            if price > j:
                break
        answer.append(sec)

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.3MB)
# 테스트 3 〉	통과 (0.72ms, 10.4MB)
# 테스트 4 〉	통과 (0.88ms, 10.2MB)
# 테스트 5 〉	통과 (1.88ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.3MB)
# 테스트 7 〉	통과 (0.38ms, 10.3MB)
# 테스트 8 〉	통과 (0.51ms, 10.1MB)
# 테스트 9 〉	통과 (0.02ms, 10.3MB)
# 테스트 10 〉	통과 (1.17ms, 10.2MB)
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