"""
Date    : 2022.01.25
Update  : 2022.01.25
Source  : 2252.py
Purpose :
url     : https://www.acmicpc.net/problem/2252
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys
from collections import deque

input = sys.stdin.readline


def topology_sort(indegree: list) -> list:
    global lines

    q = deque()

    '''
    enumerate로 q에 student를 삽입하면, 0번째 인덱스가 반드시 들어가는 비효율적인 구조가 되어서, range로 변경함.
    '''
    # for i, value in enumerate(indegree):
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    answer = []

    while q:
        student = q.popleft()
        answer.append(student)

        for next_student in lines[student]:
            indegree[next_student] -= 1

            if indegree[next_student] == 0:
                q.append(next_student)

    return answer[::-1]


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    lines = [[] for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]

    for _ in range(m):
        A, B = list(map(int, input().split()))
        lines[B].append(A)
        indegree[A] += 1

    print(*topology_sort(indegree))