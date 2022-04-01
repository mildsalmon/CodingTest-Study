"""
Date    : 2022.04.01
Update  : 2022.04.01
Source  : 네트워크.py
Purpose : dfs
url     : https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
def dfs(i, visited, computers):
    visited[i] = True

    for j in range(len(computers)):
        if computers[i][j] == 1 and not visited[j]:
            dfs(j, visited, computers)


def solution(n, computers):
    global answer

    answer = 0
    visited = [False for _ in range(n)]

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, computers)
            answer += 1

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (0.03ms, 10MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.15ms, 10.4MB)
# 테스트 7 〉	통과 (0.03ms, 10.3MB)
# 테스트 8 〉	통과 (0.10ms, 10.1MB)
# 테스트 9 〉	통과 (0.07ms, 10.2MB)
# 테스트 10 〉	통과 (0.07ms, 10.3MB)
# 테스트 11 〉	통과 (1.00ms, 10.2MB)
# 테스트 12 〉	통과 (0.41ms, 10MB)
# 테스트 13 〉	통과 (0.20ms, 10.1MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0