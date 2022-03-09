"""
Date    : 2022.03.08
Update  : 2022.03.08
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
        self.easy_questions = []
        self.hard_questions = []
        self.solved_questions = dict()

    def add(self, P, L):
        self.solved_questions[P] = L
        heapq.heappush(self.easy_questions, [L, P])
        heapq.heappush(self.hard_questions, [-L, -P])

    def recommend(self, x):
        if x == 1:
            while self.solved_questions[-self.hard_questions[0][1]] != -self.hard_questions[0][0]:
                heapq.heappop(self.hard_questions)
            return -self.hard_questions[0][1]
        else:
            while self.solved_questions[self.easy_questions[0][1]] != self.easy_questions[0][0]:
                heapq.heappop(self.easy_questions)
            return self.easy_questions[0][1]

    def solved(self, P):
        self.solved_questions[P] = 0


if __name__ == "__main__":
    recommend_system = RecommendSystem()
    n = int(input())

    for _ in range(n):
        temp = list(map(int, input().split()))
        recommend_system.add(temp[0], temp[1])

    m = int(input())

    for _ in range(m):
        command, *temp = input().split()
        temp = list(map(int, temp))

        if command == 'add':
            recommend_system.add(temp[0], temp[1])
        elif command == 'recommend':
            print(recommend_system.recommend(temp[0]))
        elif command == 'solved':
            recommend_system.solved(temp[0])