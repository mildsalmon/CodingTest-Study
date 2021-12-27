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
    temp = [(priority, i) for i, priority in enumerate(priorities)]

    q = deque(temp)

    answer = 0

    while q:
        x, i = q.popleft()

        temp = [x < i[0] for i in q]

        if any(temp):
            q.append((x, i))
        else:
            answer += 1

            if location == i:
                break

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.22ms, 10.3MB)
# 테스트 2 〉	통과 (1.83ms, 10.2MB)
# 테스트 3 〉	통과 (0.13ms, 10.3MB)
# 테스트 4 〉	통과 (0.06ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.17ms, 10.2MB)
# 테스트 7 〉	통과 (0.19ms, 10.4MB)
# 테스트 8 〉	통과 (1.24ms, 10.3MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)
# 테스트 10 〉	통과 (0.19ms, 10.3MB)
# 테스트 11 〉	통과 (0.91ms, 10.2MB)
# 테스트 12 〉	통과 (0.05ms, 10.3MB)
# 테스트 13 〉	통과 (0.97ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.02ms, 10.2MB)
# 테스트 16 〉	통과 (0.06ms, 10.2MB)
# 테스트 17 〉	통과 (1.50ms, 10.2MB)
# 테스트 18 〉	통과 (0.02ms, 10.2MB)
# 테스트 19 〉	통과 (1.04ms, 10.3MB)
# 테스트 20 〉	통과 (0.17ms, 10.3MB)

# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0