"""
Date    : 2021.12.27
Update  : 2021.12.27
Source  : 프린터.py
Purpose : 큐로 풀었다. (any()를 활용하였다.)
url     : https://programmers.co.kr/learn/courses/30/lessons/42587
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
from collections import deque


def solution(priorities, location):
    q = deque([(i, x) for i, x in enumerate(priorities)])
    cnt = 0

    while q:
        index, J = q.popleft()

        if q:
            _max = max(q, key=lambda x: x[1])[1]

            if _max > J:
                q.append((index, J))
                continue

        cnt += 1

        if index == location:
            break

    return cnt

# 정확성  테스트
# 테스트 1 〉	통과 (0.33ms, 10.2MB)
# 테스트 2 〉	통과 (2.60ms, 10.2MB)
# 테스트 3 〉	통과 (0.17ms, 9.97MB)
# 테스트 4 〉	통과 (0.08ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.24ms, 10.1MB)
# 테스트 7 〉	통과 (0.27ms, 10.2MB)
# 테스트 8 〉	통과 (1.73ms, 10.2MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)
# 테스트 10 〉	통과 (0.27ms, 10.2MB)
# 테스트 11 〉	통과 (1.27ms, 10MB)
# 테스트 12 〉	통과 (0.07ms, 10.2MB)
# 테스트 13 〉	통과 (1.11ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.1MB)
# 테스트 15 〉	통과 (0.02ms, 10.1MB)
# 테스트 16 〉	통과 (0.14ms, 10.2MB)
# 테스트 17 〉	통과 (2.20ms, 10.3MB)
# 테스트 18 〉	통과 (0.03ms, 10.2MB)
# 테스트 19 〉	통과 (1.51ms, 10.2MB)
# 테스트 20 〉	통과 (0.23ms, 10.2MB)

# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0