"""
Date    : 2022.02.23
Update  : 2022.02.23
Source  : 13022.py
Purpose :
url     : https://www.acmicpc.net/problem/13022
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import re


def solution(text):
    if len(text) % 4 != 0:
        return 0

    cnt = len(text) // 4

    for i in range(cnt, 0, -1):
        text = re.sub(rf'w{{{i}}}o{{{i}}}l{{{i}}}f{{{i}}}', '', text)

    if len(text) != 0:
        return 0
    return 1


if __name__ == "__main__":
    print(solution(input()))