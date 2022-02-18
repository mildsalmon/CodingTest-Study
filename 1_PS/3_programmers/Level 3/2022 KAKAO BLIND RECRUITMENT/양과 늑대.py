"""
Date    : 2022.02.18
Update  : 2022.02.18
Source  : 양과 늑대.py
Purpose : dfs / 비트마스킹
url     : https://programmers.co.kr/learn/courses/30/lessons/92343
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def dfs(node: int, way: list, visited: list, wolf: int, sheep: int) -> None:
    global graph, answer, copy_info

    if visited[node]:
        return
    visited[node] = True

    if copy_info[node] == 0:
        sheep += 1
        answer = max(answer, sheep)
    elif copy_info[node] == 1:
        wolf += 1

    if sheep <= wolf:
        return

    way.extend(graph[node])

    for next_node in way:
        new_way = []

        for w in way:
            if w == next_node:
                continue
            if visited[w]:
                continue
            new_way.append(w)

        dfs(next_node, new_way, visited[:], wolf, sheep)


def solution(info, edges):
    global graph, answer, copy_info

    copy_info = info[:]
    answer = 0
    graph = [[] for _ in range(len(info))]
    visited = [False for _ in range(len(info))]

    for edge in edges:
        parent, child = edge

        graph[parent].append(child)

    wolf = 0
    sheep = 0
    node = 0
    way = []

    dfs(node, way, visited, wolf, sheep)

    return answer

# 채점을 시작합니다.
#
# 정확성  테스트
#
# 테스트 1 〉	통과 (0.01ms, 10.4MB)
# 테스트 2 〉	통과 (0.19ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.23ms, 10.2MB)
# 테스트 6 〉	통과 (0.20ms, 10.2MB)
# 테스트 7 〉	통과 (0.05ms, 10.3MB)
# 테스트 8 〉	통과 (0.05ms, 10.2MB)
# 테스트 9 〉	통과 (0.46ms, 10.4MB)
# 테스트 10 〉	통과 (5.28ms, 10.4MB)
# 테스트 11 〉	통과 (0.16ms, 10.2MB)
# 테스트 12 〉	통과 (1.33ms, 10.2MB)
# 테스트 13 〉	통과 (0.03ms, 10.2MB)
# 테스트 14 〉	통과 (0.05ms, 10.4MB)
# 테스트 15 〉	통과 (0.42ms, 10.3MB)
# 테스트 16 〉	통과 (0.74ms, 10.4MB)
# 테스트 17 〉	통과 (11.07ms, 10.2MB)
# 테스트 18 〉	통과 (0.51ms, 10.3MB)
#
# 채점 결과
#
# 정확성: 100.0
# 합계: 100.0 / 100.0