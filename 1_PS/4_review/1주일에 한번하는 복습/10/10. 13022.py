"""
Date    : 2022.02.27
Update  : 2022.02.27
Source  : 10. 13022.py
Purpose : 정규식
url     : https://www.acmicpc.net/problem/13022
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import re


def check_word(s):
    if len(s) % 4:
        return False

    n = len(s) // 4

    for i in range(n, 0, -1):
        s = re.sub(rf'w{{{i}}}o{{{i}}}l{{{i}}}f{{{i}}}', '', s)

    if len(s):
        return False
    else:
        return True


if __name__ == "__main__":
    s = input()

    if check_word(s):
        print(1)
    else:
        print(0)