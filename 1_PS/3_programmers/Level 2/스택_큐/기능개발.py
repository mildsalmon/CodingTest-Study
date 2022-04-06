"""
Date    : 2021.11.07
Update  : 2022.04.06
Source  : 기능개발.py
Purpose : 스택과 큐를 이용한 문제
url     : https://programmers.co.kr/learn/courses/30/lessons/42586
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from collections import deque


def solution(progresses, speeds):
    answer = []
    q = deque()

    for progress, speed in zip(progresses, speeds):
        progress = 100 - progress
        day = round(progress / speed + 0.4)
        q.append(day)

    while q:
        day = q.popleft()
        cnt = 1

        while q and day >= q[0]:
            q.popleft()
            cnt += 1

        answer.append(cnt)

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.03ms, 10.3MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (0.02ms, 10.3MB)
# 테스트 10 〉	통과 (0.02ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0