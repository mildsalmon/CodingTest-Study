"""
Date    : 2022.03.08
Update  : 2022.03.11
Source  : 21939.py
Purpose : 우선순위 큐 / dict
url     : https://www.acmicpc.net/problem/21939
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys
import heapq

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    hard_problems = []
    easy_problems = []
    problems = dict()

    for _ in range(n):
        p, l = list(map(int, input().split()))

        heapq.heappush(hard_problems, (-l, -p))
        heapq.heappush(easy_problems, (l, p))
        problems[p] = l

    for m in range(int(input())):
        command, *temp = input().split()
        temp = list(map(int, temp))

        if command == 'add':
            heapq.heappush(hard_problems, (-temp[1], -temp[0]))
            heapq.heappush(easy_problems, (temp[1], temp[0]))
            problems[temp[0]] = temp[1]
        elif command == 'recommend':
            if temp[0] == 1:
                while problems[-hard_problems[0][1]] != -hard_problems[0][0]:
                    heapq.heappop(hard_problems)
                print(-hard_problems[0][1])
            elif temp[0] == -1:
                while problems[easy_problems[0][1]] != easy_problems[0][0]:
                    heapq.heappop(easy_problems)
                print(easy_problems[0][1])
        elif command == 'solved':
            problems[temp[0]] = 0

