"""
Date    : 2022.04.11
Update  : 2022.04.11
Source  : [1차] 비밀지도.py
Purpose : 2진수 / 구현
url     : https://programmers.co.kr/learn/courses/30/lessons/17681
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def solution(n, arr1, arr2):
    answer = []

    for a, b in zip(arr1, arr2):
        temp = bin(a | b)[2:]
        temp = temp.rjust(n, '0')
        temp = temp.replace('1', '#')
        temp = temp.replace('0', ' ')
        answer.append(temp)

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.1MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0