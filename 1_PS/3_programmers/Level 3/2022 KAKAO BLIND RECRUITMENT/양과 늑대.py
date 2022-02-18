"""
Date    : 2022.02.18
Update  : 2022.02.18
Source  : 양과 늑대.py
Purpose : dfs
url     : https://programmers.co.kr/learn/courses/30/lessons/92343
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


from collections import deque


def solution(info, edges):
    answer = 0
    graph = [[] for _ in range(len(info))]
    visited = [False for _ in range(len(info))]

    for edge in edges:
        parent, child = edge

        graph[parent].append(child)

    wolf = 0
    sheep = 1
    q = deque()

    visited[0] = True
    for next_node in graph[0]:
        q.append([visited[:], next_node, wolf, sheep])

    while q:
        # print(q)
        visit, node, wolf, sheep = q.popleft()

        if info[node] == 0:
            sheep += 1
            answer = max(answer, sheep)
        elif info[node] == 1:
            wolf += 1

        if sheep <= wolf:
            continue

        visit[node] = True

        for i, v in enumerate(visit):
            if v:
                for next_node in graph[i]:
                    if not visit[next_node]:
                        q.append([visit, next_node, wolf, sheep])
    return answer

# 채점을 시작합니다.
#
# 정확성  테스트
#
# 테스트 1 〉	실패 (0.01ms, 10.3MB)
# 테스트 2 〉	실패 (0.40ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	실패 (0.37ms, 10.2MB)
# 테스트 6 〉	실패 (0.15ms, 10.4MB)
# 테스트 7 〉	실패 (0.10ms, 10.2MB)
# 테스트 8 〉	실패 (0.28ms, 10.2MB)
# 테스트 9 〉	통과 (0.57ms, 10.3MB)
# 테스트 10 〉	통과 (0.85ms, 10.2MB)
# 테스트 11 〉	실패 (0.74ms, 10MB)
# 테스트 12 〉	실패 (0.71ms, 10.2MB)
# 테스트 13 〉	실패 (0.18ms, 10.2MB)
# 테스트 14 〉	실패 (0.21ms, 10.2MB)
# 테스트 15 〉	실패 (0.41ms, 10.2MB)
# 테스트 16 〉	실패 (1.24ms, 10MB)
# 테스트 17 〉	통과 (1.14ms, 10.2MB)
# 테스트 18 〉	통과 (0.10ms, 10.3MB)
#
# 채점 결과
#
# 정확성: 33.3
# 합계: 33.3 / 100.0