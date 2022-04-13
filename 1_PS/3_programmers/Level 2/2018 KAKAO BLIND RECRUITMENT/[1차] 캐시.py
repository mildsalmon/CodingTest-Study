"""
Date    : 2022.04.13
Update  : 2022.04.13
Source  : [1차] 캐시.py
Purpose : Linked List / LRU / stack / list / queue
url     : https://programmers.co.kr/learn/courses/30/lessons/17680
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
from collections import deque


def solution(cacheSize, cities):
    answer = 0
    # deque에 maxlen 파라미터가 있다 !!
    q = deque(maxlen=cacheSize)

    for city in cities:
        city = city.lower()

        if city in q:
            answer += 1
            # deque에 list.pop(0)처럼 중간 값을 지우는 remove가 있다. !!
            q.remove(city)
            q.append(city)
        else:
            answer += 5
            q.append(city)

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.03ms, 10.2MB)
# 테스트 11 〉	통과 (74.21ms, 17.5MB)
# 테스트 12 〉	통과 (0.04ms, 10.1MB)
# 테스트 13 〉	통과 (0.04ms, 10.2MB)
# 테스트 14 〉	통과 (0.06ms, 10.2MB)
# 테스트 15 〉	통과 (0.13ms, 10.2MB)
# 테스트 16 〉	통과 (0.11ms, 10.2MB)
# 테스트 17 〉	통과 (0.13ms, 10.2MB)
# 테스트 18 〉	통과 (0.29ms, 10.3MB)
# 테스트 19 〉	통과 (0.45ms, 10.3MB)
# 테스트 20 〉	통과 (0.60ms, 10.2MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0