"""
Date    : 2022.02.20
Update  : 2022.02.20
Source  : 2870.py
Purpose : re / 문자열 / 파싱
url     : https://www.acmicpc.net/problem/2870
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import re

if __name__ == "__main__":
    n = int(input())
    arr = [input() for _ in range(n)]
    re_arr = []

    for s in arr:
        temp = re.sub(r'\D', ' ', s)

        for t in temp.split():
            re_arr.append(int(t))

    re_arr.sort()

    print(*re_arr, sep='\n')