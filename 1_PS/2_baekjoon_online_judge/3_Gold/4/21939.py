"""
Date    : 2022.03.08
Update  : 2022.03.13
Source  : 21939.py
Purpose : 우선순위 큐 / dict
url     : https://www.acmicpc.net/problem/21939
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys
import heapq

input = sys.stdin.readline


class RecommendSystem:
    def __init__(self):
        self.num_by_level = dict()
        self.hard_problems = []
        self.easy_problems = []

    def add(self, P, L):
        self.num_by_level[P] = L
        heapq.heappush(self.hard_problems, (-L, -P))
        heapq.heappush(self.easy_problems, (L, P))

    def recommend(self, x):
        if x == 1:
            while -self.hard_problems[0][0] != self.num_by_level[-self.hard_problems[0][1]]:
                heapq.heappop(self.hard_problems)
            return -self.hard_problems[0][1]
        elif x == -1:
            while self.easy_problems[0][0] != self.num_by_level[self.easy_problems[0][1]]:
                heapq.heappop(self.easy_problems)
            return self.easy_problems[0][1]

    def solved(self, P):
        self.num_by_level[P] = 0


if __name__ == "__main__":
    n = int(input())
    recommend_system = RecommendSystem()

    for _ in range(n):
        P, L = list(map(int, input().split()))
        recommend_system.add(P, L)

    m = int(input())

    for _ in range(m):
        command, *problem_info = input().split()
        problem_info = list(map(int, problem_info))

        if command == 'add':
            recommend_system.add(problem_info[0], problem_info[1])
        elif command == 'recommend':
            P = recommend_system.recommend(problem_info[0])
            print(P)
        elif command == 'solved':
            recommend_system.solved(problem_info[0])

