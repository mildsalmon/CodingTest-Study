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

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    questions = []

    for _ in range(n):
        temp = list(map(int, input().split()))
        questions.append(temp)
    questions.sort(key=lambda x: -x[1])

    m = int(input())

    for _ in range(m):
        command, *temp = input().split()
        temp = list(map(int, temp))

        if command == 'add':
            questions.append(temp)
            questions.sort(key=lambda x: -x[1])
        elif command == 'recommend':
            rank = temp[0]
            if rank == 1:
                rank = 0
            print(questions[rank][0])
        elif command == 'solved':
            question = temp[0]

            for i, value in enumerate(questions):
                if value[0] == question:
                    questions.pop(i)
                    break