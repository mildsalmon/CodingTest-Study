"""
Date    : 2022.03.15
Update  : 2022.03.20
Source  : 20210.py
Purpose : 정렬 / timsort / re
url     : https://www.acmicpc.net/problem/20210
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import re
import functools


def split_str_num(s: str) -> list:
    com = re.compile(r'[A-Za-z]|\d+')
    return re.findall(com, s)


def decision(x, y) -> int:
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0


def cmp(a, b) -> int:
    """
    a가 크면 1, 같으면 0, 작으면 -1
    """
    for a_element, b_element in zip(a, b):
        if a_element == b_element:
            continue

        if a_element.isdigit() and b_element.isdigit():
            if int(a_element) == int(b_element):
                # 숫자가 같은거니 0의 개수 카운트
                return decision(len(a_element), len(b_element))
            else:
                return decision(int(a_element), int(b_element))
        elif a_element.isalpha() and b_element.isalpha():
            if a_element.lower() == b_element.lower():
                return decision(a_element, b_element)
            else:
                return decision(a_element.lower(), b_element.lower())
        else:
            if a_element.isdigit():
                return -1
            elif b_element.isdigit():
                return 1
    return decision(len(a), len(b))


if __name__ == "__main__":
    n = int(input())
    files = [split_str_num(input()) for _ in range(n)]
    files.sort()
    files.sort(key=functools.cmp_to_key(cmp))

    print(*list(map(lambda x: ''.join(x), files)), sep='\n')