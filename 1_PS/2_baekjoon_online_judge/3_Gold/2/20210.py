"""
Date    : 2022.03.15
Update  : 2022.03.15
Source  : 20210.py
Purpose : 정렬 / timsort / re
url     : https://www.acmicpc.net/problem/20210
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import functools
import re


def alpha_num_grouping(s: str) -> list:
    com = re.compile(r'[a-zA-Z]|\d+')
    return re.findall(com, s)


def func(a, b) -> int:
    if a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 1


def cmp(a, b) -> int:
    """
    a와 b를 비교했을 때, a가 더 크면 1 / 같으면 0 / 작으면 -1
    """
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            continue

        if a[i].isdigit() and b[i].isdigit():
            # 둘 다 숫자
            if int(a[i]) == int(b[i]):
                return func(len(a[i]), len(b[i]))
            else:
                return func(int(a[i]), int(b[i]))
        elif not a[i].isdigit() and not b[i].isdigit():
            # 둘 다 문자
            if a[i].lower() == b[i].lower():
                return func(a[i], b[i])
            else:
                return func(a[i].lower(), b[i].lower())
        else:
            # 숫자 문자 / 문자 숫자
            if a[i].isdigit():
                return -1
            else:
                return 1

    return func(len(a), len(b))


if __name__ == "__main__":
    n = int(input())
    strs = [alpha_num_grouping(input()) for _ in range(n)]

    # print(*strs, sep='\n')
    # print()

    strs.sort(key=functools.cmp_to_key(cmp))

    for s in strs:
        print(''.join(s))