"""
Date    : 2022.02.23
Update  : 2022.02.23
Source  : 13022.py
Purpose :
url     : https://www.acmicpc.net/problem/13022
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def solution(text):
    if len(text) % 4 != 0:
        return 0

    cnt = len(text) // 4

    for i in range(cnt, 0, -1):
        text = text.replace(f'{"w"*i}{"o"*i}{"l"*i}{"f"*i}', '')

    if len(text) != 0:
        return 0
    return 1


if __name__ == "__main__":
    print(solution(input()))