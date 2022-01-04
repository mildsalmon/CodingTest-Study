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

def solution(scoville: list, K: int) -> int:
    heapq.heapify(scoville)
    count = 0

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1

        food_A = heapq.heappop(scoville)
        food_B = heapq.heappop(scoville)

        mix_food = food_A + 2 * food_B

        heapq.heappush(scoville, mix_food)
        count += 1

    return count

# 정확성  테스트
#
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.72ms, 10.2MB)
# 테스트 7 〉	통과 (0.68ms, 10.2MB)
# 테스트 8 〉	통과 (0.05ms, 10.2MB)
# 테스트 9 〉	통과 (0.09ms, 10.2MB)
# 테스트 10 〉	통과 (0.29ms, 10.2MB)
# 테스트 11 〉	통과 (0.19ms, 10.3MB)
# 테스트 12 〉	통과 (1.36ms, 10.2MB)
# 테스트 13 〉	통과 (0.36ms, 10.4MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.70ms, 10.3MB)
# 테스트 16 〉	통과 (0.00ms, 10.2MB)
#
# 효율성  테스트
#
# 테스트 1 〉	통과 (185.94ms, 16.2MB)
# 테스트 2 〉	통과 (397.80ms, 22MB)
# 테스트 3 〉	통과 (1828.42ms, 49.7MB)
# 테스트 4 〉	통과 (143.68ms, 15MB)
# 테스트 5 〉	통과 (1644.89ms, 51.9MB)
#
# 채점 결과
#
# 정확성: 76.2
# 효율성: 23.8
# 합계: 100.0 / 100.0