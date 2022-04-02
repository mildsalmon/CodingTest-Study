"""
Date    : 2022.04.02
Update  : 2022.04.03
Source  : 여행경로.py
Purpose : dfs
url     : https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def dfs(depth, route, n, tickets, visited):
    global answer

    if len(route) == n:
        answer.append(route)
        return

    visited[depth] = True

    for i, ticket in enumerate(tickets):
        if visited[i]:
            continue
        if ticket[0] == route[-1]:
            dfs(i, route + [ticket[1]], n, tickets, visited)
    visited[depth] = False


def solution(tickets):
    global answer

    answer = []
    n = len(tickets) + 1
    visited = [False for _ in range(len(tickets))]

    for i, ticket in enumerate(tickets):
        if ticket[0] == 'ICN':
            dfs(i, ticket[:], n, tickets, visited)

    answer.sort()

    return answer[0]

# 정확성  테스트
# 테스트 1 〉	통과 (293.51ms, 14.6MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0