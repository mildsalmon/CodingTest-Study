"""
Date    : 2022.02.16
Update  : 2022.02.16
Source  : 양궁대회.py
Purpose : 재귀 / dfs / 그리디 / 시뮬레이션
url     : https://programmers.co.kr/learn/courses/30/lessons/92342
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def check_point(apeach, lion):
    apeach_point = 0
    lion_point = 0
    max_point = len(apeach) - 1

    for i in range(max_point):
        if apeach[i] >= lion[i]:
            if apeach[i] != 0:
                apeach_point += (max_point - i)
        else:
            lion_point += (max_point - i)

    return apeach_point, lion_point


def recursive(info, lion_info, last_point, n, i):
    global max_point, answer

    if i < 0 or last_point <= 0:
        if last_point > 0:
            lion_info[-1] = last_point
        # print(f"1. {lion_info}")
        # print(f"last {last_point}")
        if sum(lion_info) == n:
            apeach, lion = check_point(info, lion_info)
            # print(apeach, lion)
            # print(lion_info)
            # *핵심*
            diff_point = lion - apeach
            if diff_point > 0:
                # *핵심*
                if max_point <= diff_point:
                    max_point = diff_point
                    answer = lion_info[:]
        lion_info[-1] = 0
        return

    recursive(info, lion_info, last_point, n, i - 1)

    if info[i] + 1 <= last_point:
        lion_info[i] = info[i] + 1
        last_point -= (info[i] + 1)

        recursive(info, lion_info, last_point, n, i - 1)

        last_point += (info[i] + 1)
        lion_info[i] = 0


def solution(n, info):
    global max_point, answer

    answer = [-1]
    max_point = -1
    lion_info = [0 for _ in range(11)]

    recursive(info, lion_info, n, n, 9)

    return answer
