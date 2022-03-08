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
from collections import defaultdict

input = sys.stdin.readline


def add(P, L):
    global easy_questions, hard_questions, solved_questions

    solved_questions[P] = False
    heapq.heappush(easy_questions, [L, P])
    heapq.heappush(hard_questions, [-L, -P])


def recommend(x):
    global easy_questions, hard_questions, solved_questions

    if x == 1:
        while solved_questions[-hard_questions[0][1]]:
            heapq.heappop(hard_questions)
        return -hard_questions[0][1]
    else:
        while solved_questions[easy_questions[0][1]]:
            heapq.heappop(easy_questions)
        return easy_questions[0][1]


def solved(P):
    global easy_questions, hard_questions, solved_questions

    solved_questions[P] = True

    while easy_questions and solved_questions[easy_questions[0][1]]:
        heapq.heappop(easy_questions)
    while hard_questions and solved_questions[-hard_questions[0][1]]:
        heapq.heappop(hard_questions)


if __name__ == "__main__":
    n = int(input())
    easy_questions = []
    hard_questions = []
    solved_questions = defaultdict(bool)

    for _ in range(n):
        temp = list(map(int, input().split()))
        add(temp[0], temp[1])

    m = int(input())

    for _ in range(m):
        command, *temp = input().split()
        temp = list(map(int, temp))

        if command == 'add':
            add(temp[0], temp[1])
        elif command == 'recommend':
            print(recommend(temp[0]))
        elif command == 'solved':
            solved(temp[0])