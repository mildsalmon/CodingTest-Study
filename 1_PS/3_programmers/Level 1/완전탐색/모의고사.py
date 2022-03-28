"""
Date    : 2022.03.28
Update  : 2022.03.28
Source  : 모의고사.py
Purpose : dfs / 완전 탐색 / 재귀
url     : https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def solution(answers):
    answer = []
    people = [[1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    cnt = [0, 0, 0]

    for i, value in enumerate(answers):
        if people[0][i % len(people[0])] == value:
            cnt[0] += 1
        if people[1][i % len(people[1])] == value:
            cnt[1] += 1
        if people[2][i % len(people[2])] == value:
            cnt[2] += 1

    _max = max(cnt)

    for i, value in enumerate(cnt):
        if _max == value:
            answer.append(i + 1)

    answer.sort()

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.03ms, 10.4MB)
# 테스트 6 〉	통과 (0.05ms, 10.2MB)
# 테스트 7 〉	통과 (1.87ms, 10.3MB)
# 테스트 8 〉	통과 (0.62ms, 10.2MB)
# 테스트 9 〉	통과 (3.35ms, 10.2MB)
# 테스트 10 〉	통과 (1.61ms, 10.3MB)
# 테스트 11 〉	통과 (3.71ms, 10.5MB)
# 테스트 12 〉	통과 (3.19ms, 10.3MB)
# 테스트 13 〉	통과 (0.20ms, 10.2MB)
# 테스트 14 〉	통과 (3.65ms, 10.4MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0