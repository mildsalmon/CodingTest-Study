"""
Date    : 2021.12.27
Update  : 2021.12.27
Source  : 프린터.py
Purpose : 큐로 풀었다.
url     : https://programmers.co.kr/learn/courses/30/lessons/42587
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from collections import deque

def solution(priorities, location):
    temp = [(priority, i) for i, priority in enumerate(priorities)]

    q = deque(temp)

    answer = []

    while q:
        x, i = q.popleft()
        # 이 부분이 마음에 들지 않는다.
        check = True

        for nx, j in q:
            if nx > x:
                q.append((x, i))
                check = False
                break
        if check:
            answer.append((x, i))

    for i in range(len(answer)):
        if answer[i][1] == location:
            # 이 부분이 마음에 들지 않는다.
            return i + 1

# 정확성  테스트
# 테스트 1 〉	통과 (0.17ms, 10.3MB)
# 테스트 2 〉	통과 (0.27ms, 10.3MB)
# 테스트 3 〉	통과 (0.20ms, 10.3MB)
# 테스트 4 〉	통과 (0.06ms, 10.4MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.05ms, 10.3MB)
# 테스트 7 〉	통과 (0.08ms, 10.3MB)
# 테스트 8 〉	통과 (0.24ms, 10.3MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.05ms, 10.2MB)
# 테스트 11 〉	통과 (0.15ms, 10.2MB)
# 테스트 12 〉	통과 (0.06ms, 10.3MB)
# 테스트 13 〉	통과 (0.15ms, 10.4MB)
# 테스트 14 〉	통과 (0.01ms, 10.3MB)
# 테스트 15 〉	통과 (0.04ms, 10.3MB)
# 테스트 16 〉	통과 (0.03ms, 10.2MB)
# 테스트 17 〉	통과 (0.42ms, 10.3MB)
# 테스트 18 〉	통과 (0.01ms, 10.3MB)
# 테스트 19 〉	통과 (0.23ms, 10.3MB)
# 테스트 20 〉	통과 (0.12ms, 10.2MB)

# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0