"""
Date    : 2022.03.24
Update  : 2022.03.24
Source  : 이중우선순위큐.py
Purpose : heapq / class
url     : https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import heapq


class DoublePriorityQueue:
    def __init__(self):
        self.max_value = []
        self.min_value = []
        self.visited = dict()

    def add_num(self, num):
        heapq.heappush(self.min_value, num)
        heapq.heappush(self.max_value, -num)
        self.visited[num] = True

    def delete_num(self, q):
        if self.empty_queue(self.min_value) or self.empty_queue(self.max_value):
            self.max_value = []
            self.min_value = []
            return

        if q == -1:
            self.visited[heapq.heappop(self.min_value)] = False
            while not self.empty_queue(self.min_value) and not self.visited[self.min_value[0]]:
                heapq.heappop(self.min_value)
        elif q == 1:
            self.visited[-heapq.heappop(self.max_value)] = False
            while not self.empty_queue(self.max_value) and not self.visited[-self.max_value[0]]:
                heapq.heappop(self.max_value)

    def empty_queue(self, q):
        if len(q):
            return False
        return True

    def check_max_min(self):
        max_q = 0
        min_q = 0

        while len(self.min_value) and not self.visited[self.min_value[0]]:
            heapq.heappop(self.min_value)
        while len(self.max_value) and not self.visited[-self.max_value[0]]:
            heapq.heappop(self.max_value)

        if len(self.max_value):
            max_q = -heapq.heappop(self.max_value)
        if len(self.min_value):
            min_q = heapq.heappop(self.min_value)

        return [max_q, min_q]


def solution(operations):
    q = DoublePriorityQueue()

    for operation in operations:
        command, value = operation.split()
        value = int(value)

        if command == 'I':
            q.add_num(value)
        elif command == 'D':
            q.delete_num(value)

    return q.check_max_min()

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