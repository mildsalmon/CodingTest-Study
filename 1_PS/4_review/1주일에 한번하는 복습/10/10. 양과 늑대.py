"""
Date    : 2022.02.27
Update  : 2022.02.27
Source  : 양과 늑대.py
Purpose : dfs / 비트마스킹
url     : https://programmers.co.kr/learn/courses/30/lessons/92343
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def dfs(node: int, wolf: int, sheep: int, way: list, visited: list) -> None:
    global graph, answer, copy_info

    if visited[node]:
        return

    visited[node] = True

    if copy_info[node] == 0:
        sheep += 1
    elif copy_info[node] == 1:
        wolf += 1

    if sheep <= wolf:
        return

    answer = max(sheep, answer)
    way.extend(graph[node])

    for next_node in way:
        next_way = []

        for w in way:
            if next_node == w:
                continue
            if visited[w]:
                continue
            next_way.append(w)

        dfs(next_node, wolf, sheep, next_way, visited[:])


def solution(info: list, edges: list) -> int:
    global graph, answer, copy_info

    copy_info = info[:]
    graph = [[] for _ in range(len(info))]
    visited = [False for _ in range(len(info))]
    answer = 0

    for edge in edges:
        parent, child = edge
        graph[parent].append(child)

    wolf = 0
    sheep = 0
    way = []
    node = 0

    dfs(node, wolf, sheep, way, visited)

    return answer
