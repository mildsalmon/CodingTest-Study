"""
Date    : 2022.04.05
Update  : 2022.04.09
Source  : 주식가격.py
Purpose : stack / brute force
url     : https://programmers.co.kr/learn/courses/30/lessons/42584
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def solution(prices):
    answer = [i for i in range(len(prices) - 1, -1, -1)]

    stocks = []

    for i in range(len(prices)):
        while stocks and prices[i] < prices[stocks[-1]]:
            temp = stocks.pop()
            answer[temp] = i - temp
        stocks.append(i)

    return answer


print(solution([1, 2, 3, 2, 3]))
print(solution([10, 1, 3, 2, 1]))

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.05ms, 10.2MB)
# 테스트 3 〉	통과 (0.38ms, 10.2MB)
# 테스트 4 〉	통과 (0.27ms, 10.3MB)
# 테스트 5 〉	통과 (0.30ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.27ms, 10.4MB)
# 테스트 8 〉	통과 (0.26ms, 10.4MB)
# 테스트 9 〉	통과 (0.02ms, 10.1MB)
# 테스트 10 〉	통과 (0.60ms, 10.4MB)
#
# 효율성  테스트
# 테스트 1 〉	통과 (28.59ms, 19.3MB)
# 테스트 2 〉	통과 (21.32ms, 17.9MB)
# 테스트 3 〉	통과 (32.11ms, 20.2MB)
# 테스트 4 〉	통과 (24.59ms, 18.8MB)
# 테스트 5 〉	통과 (18.96ms, 17.3MB)
#
# 채점 결과
# 정확성: 66.7
# 효율성: 33.3
# 합계: 100.0 / 100.0