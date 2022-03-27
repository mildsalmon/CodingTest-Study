"""
Date    : 2022.03.24
Update  : 2022.03.27
Source  : 이중우선순위큐.py
Purpose : heapq / class
url     : https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import heapq
from collections import defaultdict


def solution(operations):
    _max = []
    _min = []
    visited = defaultdict(int)

    for operation in operations:
        command, num = map(lambda x: x if x.isalpha() else int(x), operation.split())

        if command == 'I':
            heapq.heappush(_min, num)
            heapq.heappush(_max, -num)
            visited[num] += 1
        elif command == 'D':
            if num == 1:
                while len(_max) and visited[-_max[0]] == 0:
                    heapq.heappop(_max)
                if len(_max):
                    temp = heapq.heappop(_max)
                    visited[-temp] -= 1
            elif num == -1:
                while len(_min) and visited[_min[0]] == 0:
                    heapq.heappop(_min)
                if len(_min):
                    temp = heapq.heappop(_min)
                    visited[temp] -= 1

    if len(_max) and len(_min):
        while visited[-_max[0]] == 0:
            heapq.heappop(_max)
        while visited[_min[0]] == 0:
            heapq.heappop(_min)
        return [-_max[0], _min[0]]

    return [0, 0]


# 정확성  테스트
# 테스트 1 〉	통과 (0.03ms, 10.3MB)
# 테스트 2 〉	통과 (0.04ms, 10.5MB)
# 테스트 3 〉	통과 (0.04ms, 10.3MB)
# 테스트 4 〉	통과 (0.03ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.4MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

print(solution(["I 6", "I 2", "I 1", "I 4", "I 5", "I 3", "D 1", "I 7", "D -1", "I 6", "D -1", "D -1"]))
print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(		["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))