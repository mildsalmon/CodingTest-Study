"""
Date    : 2021.11.07
Update  : 2021.12.17
Source  : 기능개발.py
Purpose : 스택과 큐를 이용한 문제
url     : https://programmers.co.kr/learn/courses/30/lessons/42586
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def solution(progresses, speeds):
    answer = []
    time = 0

    """
    최악의 경우 while문을 100번 반복한다.
    """
    while progresses:
        time += 1
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        count = 0

        for i in range(len(progresses)):
            if progresses[i] >= 100:
                count += 1
            else:
                break

        if count > 0:
            answer.append(count)

        for _ in range(count):
            progresses.pop(0)
            speeds.pop(0)

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.59ms, 10.3MB)
# 테스트 3 〉	통과 (0.47ms, 10.1MB)
# 테스트 4 〉	통과 (0.38ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.10ms, 10.4MB)
# 테스트 7 〉	통과 (0.44ms, 10.2MB)
# 테스트 8 〉	통과 (0.14ms, 10.2MB)
# 테스트 9 〉	통과 (0.35ms, 10.2MB)
# 테스트 10 〉	통과 (0.31ms, 10.2MB)
# 테스트 11 〉	통과 (0.02ms, 10.3MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0