"""
Date    : 2022.01.05
Update  : 2022.01.06
Source  : 리모컨.py
Purpose :
url     : https://www.acmicpc.net/problem/1107
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def move_channel(channel):
    global n, available_button, min_push_button

    for button in available_button:
        temp_channel = channel + button
        min_push_button = min(min_push_button, len(temp_channel) + abs(int(n) - int(temp_channel)))
        # 채널이 최대 500_000개라서 채널은 0 <= x <= 999_999 사이의 범위에서만 이동할 수 있음
        if len(temp_channel) < 6:
            move_channel(temp_channel)

if __name__ == "__main__":
    n: str = input()
    m: int = int(input())

    if m:
        trouble_button = set(input().split())
    else:
        trouble_button = set()

    # +, -로만 채널을 이동하는 경우
    min_push_button = abs(100 - int(n))

    if min_push_button:
        # 고장난 버튼이 없을때, 3번 채널로 옮기는 경우 -> +,- 버튼만으로는 97번 / 버튼 누르는걸로 1번
        if len(trouble_button) == 0:
            min_push_button = min(min_push_button, len(n))
        else:
            available_button = set(map(str, range(0,10))).difference(trouble_button)
            move_channel('')

    print(min_push_button)