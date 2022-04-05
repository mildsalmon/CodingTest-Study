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
    answer = [i for i in range(len(prices) - 1, -1, -1)]
    stack = []

    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.1MB)
# 테스트 3 〉	통과 (0.21ms, 10.2MB)
# 테스트 4 〉	통과 (0.25ms, 10.2MB)
# 테스트 5 〉	통과 (0.29ms, 10.1MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.15ms, 10.3MB)
# 테스트 8 〉	통과 (0.18ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.1MB)
# 테스트 10 〉	통과 (0.30ms, 10.3MB)
#
# 효율성  테스트
# 테스트 1 〉	통과 (27.03ms, 19.3MB)
# 테스트 2 〉	통과 (20.30ms, 17.9MB)
# 테스트 3 〉	통과 (30.46ms, 20.1MB)
# 테스트 4 〉	통과 (42.19ms, 18.7MB)
# 테스트 5 〉	통과 (16.58ms, 17.2MB)
#
# 채점 결과
# 정확성: 66.7
# 효율성: 33.3
# 합계: 100.0 / 100.0