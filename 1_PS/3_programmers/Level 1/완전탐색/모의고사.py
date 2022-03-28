"""
Date    : 2022.03.28
Update  : 2022.03.28
Source  : 모의고사.py
Purpose : dfs / 완전 탐색 / 재귀
url     : https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def search(depth, cnt, people, correct, i):
    global answer

    if depth == len(answer):
        cnt.append([correct, i])
        return

    if answer[depth] == people[depth]:
        search(depth + 1, cnt, people, correct + 1, i)
    else:
        search(depth + 1, cnt, people, correct, i)


def high_score(cnt):
    high_score = []

    high_score.append(cnt[0][1])
    _max = cnt[0][0]

    for i in range(1, len(cnt)):
        if cnt[i][0] == _max:
            high_score.append(cnt[i][1])
        else:
            break
    high_score.sort()

    return high_score


def solution(answers):
    global answer

    answer = answers[:]

    people = []
    people.append(list(range(1, 6)) * (10000 // 5))
    people.append([2, 1, 2, 3, 2, 4, 2, 5] * (10000 // 8))
    people.append([3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (10000 // 10))

    cnt = []
    for i in range(3):
        search(0, cnt, people[i], 0, i + 1)

    cnt.sort(reverse=True)
    people = high_score(cnt)

    return people

# 정확성  테스트
# 테스트 1 〉	통과 (0.17ms, 10.1MB)
# 테스트 2 〉	통과 (0.16ms, 10.3MB)
# 테스트 3 〉	통과 (0.16ms, 10.3MB)
# 테스트 4 〉	통과 (0.16ms, 10.2MB)
# 테스트 5 〉	통과 (0.20ms, 10.2MB)
# 테스트 6 〉	통과 (0.20ms, 10.3MB)
# 테스트 7 〉	실패 (런타임 에러)
# 테스트 8 〉	실패 (런타임 에러)
# 테스트 9 〉	실패 (런타임 에러)
# 테스트 10 〉	실패 (런타임 에러)
# 테스트 11 〉	실패 (런타임 에러)
# 테스트 12 〉	실패 (런타임 에러)
# 테스트 13 〉	통과 (0.75ms, 10.5MB)
# 테스트 14 〉	실패 (런타임 에러)
#
# 채점 결과
# 정확성: 50.0
# 합계: 50.0 / 100.0