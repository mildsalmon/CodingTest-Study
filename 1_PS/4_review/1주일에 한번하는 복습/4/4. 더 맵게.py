"""
Date    : 2022.01.09
Update  : 2022.01.09
Source  : 4. 더 맵게.py
Purpose : 재귀
url     : https://programmers.co.kr/learn/courses/30/lessons/42626
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        else:
            answer += 1
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            new = a + (b * 2)
            heapq.heappush(scoville, new)

    return answer