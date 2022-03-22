"""
Date    : 2022.01.04
Update  : 2022.03.22
Source  : 더 맵게.py
Purpose : heap / heapify
url     : https://programmers.co.kr/learn/courses/30/lessons/42626
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1

        non_spicy_1 = heapq.heappop(scoville)
        non_spicy_2 = heapq.heappop(scoville)
        new_scoville = non_spicy_1 + (non_spicy_2 * 2)

        heapq.heappush(scoville, new_scoville)
        answer += 1

    return answer

# 정확성  테스트
#
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.00ms, 10.1MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.44ms, 10.1MB)
# 테스트 7 〉	통과 (0.36ms, 10.1MB)
# 테스트 8 〉	통과 (0.08ms, 10.2MB)
# 테스트 9 〉	통과 (0.06ms, 10.3MB)
# 테스트 10 〉	통과 (0.30ms, 10.2MB)
# 테스트 11 〉	통과 (0.19ms, 10.1MB)
# 테스트 12 〉	통과 (0.69ms, 10.1MB)
# 테스트 13 〉	통과 (0.36ms, 10.1MB)
# 테스트 14 〉	통과 (0.02ms, 10.1MB)
# 테스트 15 〉	통과 (0.49ms, 10.1MB)
# 테스트 16 〉	통과 (0.00ms, 10.1MB)
#
# 효율성  테스트
# 테스트 1 〉	통과 (181.41ms, 16.3MB)
# 테스트 2 〉	통과 (350.12ms, 21.9MB)
# 테스트 3 〉	통과 (1870.59ms, 49.7MB)
# 테스트 4 〉	통과 (143.50ms, 14.9MB)
# 테스트 5 〉	통과 (1879.71ms, 51.8MB)
#
# 채점 결과
#
# 정확성: 76.2
# 효율성: 23.8
# 합계: 100.0 / 100.0