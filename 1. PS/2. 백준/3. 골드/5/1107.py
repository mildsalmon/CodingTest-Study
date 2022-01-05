"""
Date    : 2022.01.05
Update  : 2022.01.05
Source  : 리모컨.py
Purpose :
url     : https://www.acmicpc.net/problem/1107
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

"""
반례

99999
2
8 9

답: 7
"""
import sys

input = sys.stdin.readline

def move_channel(depth, remote_control, channel):
    global n, min_push_button

    # 종료조건
    if depth == len(str(n)):
        min_push_button = min(min_push_button, depth + abs(int(channel) - n))
        return

    # 완전탐색
    for i in range(10):
        if remote_control[i]:
            move_channel(depth+1, remote_control, channel + str(i))


if __name__ == "__main__":
    n: int = int(input())
    m: int = int(input())
    trouble_button = set(map(int, input().split()))

    remote_control = [False if i in trouble_button else True for i in range(10)]

    min_push_button = abs(100 - n)

    if min_push_button != 0:
        move_channel(0, remote_control, '')

    print(min_push_button)