"""
Date    : 2022.04.13
Update  : 2022.04.13
Source  : [1차] 캐시.py
Purpose : Linked List / LRU / stack / list / queue
url     : https://programmers.co.kr/learn/courses/30/lessons/17680
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def is_max(q, cachesize):
    if len(q) == cachesize:
        return True
    return False


def solution(cacheSize, cities):
    answer = 0
    # q의 크기가 최대 30이라서 속도 문제가 발생하지 않은 듯
    q = []

    for city in cities:
        city = city.lower()

        if city in q:
            answer += 1
            q.append(q.pop(q.index(city)))
        else:
            answer += 5

            if cacheSize != 0:
                if is_max(q, cacheSize):
                    q.pop(0)
                q.append(city)

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.3MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.03ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.1MB)
# 테스트 8 〉	통과 (0.02ms, 10.2MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0