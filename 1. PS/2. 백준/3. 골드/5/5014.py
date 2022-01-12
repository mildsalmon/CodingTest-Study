"""
Date    : 2022.01.12
Update  : 2022.01.12
Source  : 5014.py
Purpose :
url     : https://www.acmicpc.net/problem/5014
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from collections import deque

def check_floor(S: int, G: int, D: int, U: int):
    if (S > G and D == 0) or (S < G and U == 0):
        # 현재층이 목표층보다 높고 내려가는 버튼이 없을 때
        # 현재층이 목표층보다 낮고 올라가는 버튼이 없을 때
        return False
    return True

def count_button(F: int, S: int, G: int, U: int, D: int) -> str:
    push_button = check_floor(S, G, D, U)

    if push_button:
        if S == G:
            return "0"

        q = deque()
        q.append(S)

        count = 0

        while q:
            now_floor = q.popleft()

            if now_floor == G:
                return str(count)

            count += 1

            if G - now_floor > 0:
                if G - now_floor < U:
                    next_floor = now_floor - D
                else:
                    next_floor = now_floor + U
            elif G - now_floor < 0:
                if abs(G - now_floor) < D:
                    next_floor = now_floor + U
                else:
                    next_floor = now_floor - D

            if 1 <= next_floor <= F:
                q.append(next_floor)

    return "use the stairs"

if __name__ == "__main__":
    F, S, G, U, D = list(map(int, input().split()))

    print(count_button(F, S, G, U, D))