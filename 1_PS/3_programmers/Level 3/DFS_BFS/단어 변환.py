"""
Date    : 2022.04.02
Update  : 2022.04.02
Source  : 단어 변환.py
Purpose : dfs
url     : https://programmers.co.kr/learn/courses/30/lessons/43163
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def check_word(original, comparison):
    len_original = len(original)
    cnt = 0

    for o, c in zip(original, comparison):
        if o == c:
            cnt += 1

    return len_original - 1 == cnt


def dfs(depth, visited, words, word, target):
    global answer

    if word == target:
        answer = min(answer, depth)
        return

    for i, value in enumerate(words):
        if not visited[i] and check_word(word, value):
            visited[i] = True
            dfs(depth + 1, visited, words, value, target)
            visited[i] = False


def solution(begin, target, words):
    global answer

    answer = 1e9
    if target not in words:
        return 0

    visited = [False for _ in range(len(words))]

    dfs(0, visited, words, begin, target)

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.4MB)
# 테스트 2 〉	통과 (0.05ms, 10.3MB)
# 테스트 3 〉	통과 (0.31ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.00ms, 10.4MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0