"""
Date    : 2022.01.05
Update  : 2022.01.05
Source  : 리모컨.py
Purpose :
url     : https://www.acmicpc.net/problem/1107
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys

# input = sys.stdin.readline().rstrip()

def move_channel(depth, remote_control, channel):
    global n, min_push_button

    # 종료조건
    if len(n) - 1 <= depth <= len(n) + 1 and len(channel) != 0:
        min_push_button = min(min_push_button, depth + abs(int(channel) - int(n)))

        if depth == len(n) + 1:
            return

    # 완전탐색
    if depth < len(n) - 1:
        bound = [i%10 for i in range(int(n[depth]) - 2, int(n[depth]) + 3)]
        # bound = [int(n[depth]) - 1, int(n[depth]), (int(n[depth]) + 2) % 10]

        for i in bound:
            if remote_control[i]:
                move_channel(depth+1, remote_control, channel + str(i))
    else:
        for i in range(10):
            if remote_control[i]:
                move_channel(depth+1, remote_control, channel + str(i))


if __name__ == "__main__":
    while True:
        n: str = input()
        m: int = int(input())

        if m == 0:
            trouble_button = set()
        else:
            trouble_button = set(map(int, input().split()))
        # print(n)
        # print(trouble_button)
        remote_control = [False if i in trouble_button else True for i in range(10)]

        min_push_button = abs(100 - int(n))

        if min_push_button != 0:
            move_channel(0, remote_control, '')

        print(min_push_button)