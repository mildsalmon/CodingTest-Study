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
        temp = set(temp)
        # any를 쓰지 않는다면, 이렇게도 풀 수 있다.
        # 위에서 set을 사용한 이유는
            # if ~ in (iterable)일 경우 set은 O(1)만에 iterable 객체의 값을 찾지만,
            # list는 O(n)만에 값을 찾기 때문에 속도 차이가 많이 발생한다.
        if True in temp:
            q.append((x, i))
        else:
            answer += 1

            if location == i:
                break

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.23ms, 10.3MB)
# 테스트 2 〉	통과 (2.10ms, 10.2MB)
# 테스트 3 〉	통과 (0.14ms, 10.2MB)
# 테스트 4 〉	통과 (0.07ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.21ms, 10.3MB)
# 테스트 7 〉	통과 (0.23ms, 10.3MB)
# 테스트 8 〉	통과 (1.37ms, 10.2MB)
# 테스트 9 〉	통과 (0.04ms, 10.2MB)
# 테스트 10 〉	통과 (0.26ms, 10.2MB)
# 테스트 11 〉	통과 (1.02ms, 10.3MB)
# 테스트 12 〉	통과 (0.06ms, 10.3MB)
# 테스트 13 〉	통과 (0.92ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.03ms, 10.2MB)
# 테스트 16 〉	통과 (0.07ms, 10.2MB)
# 테스트 17 〉	통과 (1.81ms, 10.2MB)
# 테스트 18 〉	통과 (0.02ms, 10.2MB)
# 테스트 19 〉	통과 (1.22ms, 10.2MB)
# 테스트 20 〉	통과 (0.18ms, 10.3MB)

# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0