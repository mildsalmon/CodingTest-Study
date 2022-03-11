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
    problems = []

    for _ in range(n):
        p, l = list(map(int, input().split()))

        problems.append((p, l))

    problems.sort(key=lambda x: [-x[1], -x[0]])
    dict_problems = dict(problems)

    for m in range(int(input())):
        command, *temp = input().split()
        temp = list(map(int, temp))

        if command == 'add':
            dict_problems[temp[0]] = temp[1]
        elif command == 'recommend':
            if temp[0] == 1:
                problems = list(map(lambda x: [-x[1], -x[0]], dict_problems.items()))
                heapq.heapify(problems)
                print(-problems[0][1])
            elif temp[0] == -1:
                problems = list(map(lambda x: [x[1], x[0]], dict_problems.items()))
                heapq.heapify(problems)
                print(problems[0][1])
        elif command == 'solved':
            dict_problems.pop(temp[0])
