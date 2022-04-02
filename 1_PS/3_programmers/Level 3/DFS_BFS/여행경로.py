"""
Date    : 2022.04.02
Update  : 2022.04.02
Source  : 여행경로.py
Purpose : dfs
url     : https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def dfs(citys, visited, tickets):
    global n, answer

    if len(citys) == n:
        answer.append(citys)
        return

    for i, ticket in enumerate(tickets):
        if not visited[i] and ticket[0] == citys[-1]:
            visited[i] = True
            dfs(citys + [ticket[1]], visited, tickets)
            visited[i] = False


def solution(tickets):
    global n, answer

    n = len(tickets) + 1
    answer = []
    visited = [False for _ in range(len(tickets))]

    for i, ticket in enumerate(tickets):
        citys = []

        if ticket[0] == 'ICN':
            visited[i] = True
            citys.extend(ticket)
            dfs(citys, visited, tickets)
            visited[i] = False
    answer.sort()

    return answer[0]

# 정확성  테스트
# 테스트 1 〉	통과 (289.84ms, 14.4MB)
# 테스트 2 〉	통과 (0.01ms, 10MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0