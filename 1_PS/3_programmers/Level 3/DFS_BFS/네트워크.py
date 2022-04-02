"""
Date    : 2022.04.01
Update  : 2022.04.03
Source  : 네트워크.py
Purpose : dfs
url     : https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def search(depth, visited, computers):
    visited[depth] = True

    for i, computer in enumerate(computers[depth]):
        if i == depth:
            continue
        if visited[i]:
            continue
        if computer == 0:
            continue
        search(i, visited, computers)


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(len(computers))]

    for i in range(len(computers)):
        if visited[i]:
            continue
        answer += 1
        search(i, visited, computers)

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.04ms, 10.2MB)
# 테스트 4 〉	통과 (0.03ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.15ms, 10.1MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.11ms, 10.1MB)
# 테스트 9 〉	통과 (0.07ms, 10.2MB)
# 테스트 10 〉	통과 (0.07ms, 10.1MB)
# 테스트 11 〉	통과 (0.52ms, 10.4MB)
# 테스트 12 〉	통과 (0.43ms, 10.2MB)
# 테스트 13 〉	통과 (0.22ms, 10.2MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0