"""
Date    : 2022.01.04
Update  : 2022.01.04
Source  : 더 맵게.py
Purpose : heap / heapify
url     : https://programmers.co.kr/learn/courses/30/lessons/42626
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0

    while min(scoville) < K:
        if len(scoville) < 2:
            return -1

        food_A = heapq.heappop(scoville)
        food_B = heapq.heappop(scoville)

        mix_food = food_A + 2 * food_B

        heapq.heappush(scoville, mix_food)
        count += 1

    return count

# 채점을 시작합니다.
#
# 정확성  테스트
#
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (3.12ms, 10.2MB)
# 테스트 7 〉	통과 (2.20ms, 10.2MB)
# 테스트 8 〉	통과 (0.11ms, 10.2MB)
# 테스트 9 〉	통과 (0.14ms, 10.4MB)
# 테스트 10 〉	통과 (1.72ms, 10.3MB)
# 테스트 11 〉	통과 (0.96ms, 10.2MB)
# 테스트 12 〉	통과 (6.58ms, 10.2MB)
# 테스트 13 〉	통과 (2.39ms, 10.2MB)
# 테스트 14 〉	통과 (0.03ms, 10.2MB)
# 테스트 15 〉	통과 (3.79ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.4MB)
#
# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)