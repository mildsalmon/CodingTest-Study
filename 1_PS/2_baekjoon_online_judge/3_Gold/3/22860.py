"""
Date    : 2022.03.10
Update  : 2022.03.11
Source  : 22860.py
Purpose : dict / dfs / 재귀 / 구현 / 문자열 / 파싱
url     : https://www.acmicpc.net/problem/22860
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys
from collections import deque

sys.setrecursionlimit(10**5)

def search_file(query: str) -> list:
    global directorys

    q = deque()
    q.append(query)

    files = set()
    files.add(query)
    kind_file_cnt = 0
    file_cnt = 0

    while q:
        node = q.popleft()

        if node not in directorys:
            continue

        for next_node, flag in directorys[node]:
            if flag == '1':
                q.append(next_node)
                continue

            if next_node in files:
                file_cnt += 1
                continue

            files.add(next_node)
            kind_file_cnt += 1
            file_cnt += 1

    return [kind_file_cnt, file_cnt]


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    directorys = dict()

    for _ in range(n + m):
        p, f, c = input().split()

        if p not in directorys:
            directorys[p] = []
        directorys[p].append((f, c))

    for q in range(int(input())):
        query = input().split('/')[-1]

        answer = search_file(query)
        print(answer[0], answer[1])
