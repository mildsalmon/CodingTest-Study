"""
Date    : 2022.01.09
Update  : 2022.01.09
Source  : 4. 리모컨.py
Purpose : 재귀
url     : https://www.acmicpc.net/problem/16637
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def move_channel(channel):
    global min_click, n, btns

    for btn in btns:
        temp = channel + btn
        min_click = min(min_click, len(temp) + abs(int(n) - int(temp)))
        if len(temp) < 6:
            move_channel(temp)


if __name__ == "__main__":
    n = input()
    m = int(input())

    btns = set(map(str, range(0, 10)))

    min_click = abs(100 - int(n))

    if m:
        break_btn = set(input().split())
        btns = btns.difference(break_btn)

        if min_click:

            move_channel('')
    else:
        min_click = min(min_click, len(n))

    print(min_click)