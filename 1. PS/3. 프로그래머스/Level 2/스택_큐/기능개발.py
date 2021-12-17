"""
Date    : 2021.11.07
Update  : 2021.12.17
Source  : 기능개발.py
Purpose : 스택과 큐를 이용한 문제
url     : https://programmers.co.kr/learn/courses/30/lessons/42586
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from collections import deque
import math


def solution(progresses, speeds):
    q = deque()

    for i, progress in enumerate(progresses):
        temp = 100 - progress
        temp = math.ceil(temp / speeds[i])
        q.append((progress, temp))

    answer = [1]
    p, time = q.popleft()

    while q:
        x_p, x_time = q.popleft()

        if x_time <= time:
            answer[-1] += 1
        elif x_time > time:
            answer.append(1)
            time = x_time

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.4MB)
# 테스트 7 〉	통과 (0.03ms, 10.1MB)
# 테스트 8 〉	통과 (0.01ms, 10.4MB)
# 테스트 9 〉	통과 (0.02ms, 10.4MB)
# 테스트 10 〉	통과 (0.03ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0