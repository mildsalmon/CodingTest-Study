"""
Date    : 2022.04.14
Update  : 2022.04.14
Source  : [1차] 뉴스 클러스터링.py
Purpose : set / dict / multiset / union / intersection
url     : https://programmers.co.kr/learn/courses/30/lessons/17677
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
from collections import defaultdict


def str_set(s):
    answer = defaultdict(int)

    for a, b in zip(s, s[1:]):
        temp = a + b
        if temp.isalpha():
            answer[temp.lower()] += 1

    return answer


def solution(str1, str2):
    s1_sub = str_set(str1)
    s2_sub = str_set(str2)

    intersection = set(s1_sub.keys()).intersection(set(s2_sub.keys()))
    union = set(s1_sub.keys()).union(set(s2_sub.keys()))

    if not union:
        return 1 * 65536

    intersection_cnt = 0
    union_cnt = 0

    for value in intersection:
        a, b = 1e9, 1e9

        if value in s1_sub:
            a = s1_sub[value]
        if value in s2_sub:
            b = s2_sub[value]

        intersection_cnt += min(a, b)

    for value in union:
        a, b = 0, 0

        if value in s1_sub:
            a = s1_sub[value]
        if value in s2_sub:
            b = s2_sub[value]

        union_cnt += max(a, b)

    return int((intersection_cnt / union_cnt) * 65536)

# 정확성  테스트
# 테스트 1 〉	통과 (0.86ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (1.10ms, 10.4MB)
# 테스트 5 〉	통과 (0.05ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.3MB)
# 테스트 7 〉	통과 (0.15ms, 10.3MB)
# 테스트 8 〉	통과 (0.03ms, 10.3MB)
# 테스트 9 〉	통과 (0.13ms, 10.4MB)
# 테스트 10 〉	통과 (0.18ms, 10.3MB)
# 테스트 11 〉	통과 (0.21ms, 10.4MB)
# 테스트 12 〉	통과 (0.01ms, 10.3MB)
# 테스트 13 〉	통과 (0.06ms, 10.4MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0