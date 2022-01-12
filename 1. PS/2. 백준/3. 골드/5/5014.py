"""
Date    : 2022.01.12
Update  : 2022.01.12
Source  : 5014.py
Purpose : bfs / visited / 사전 종료 조건
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

        count = 0

        q = deque()
        q.append((count, S))

        visited = [False] * (F+1)

        while q:
            count, now_floor = q.popleft()

            if now_floor == G:
                return str(count)

            count += 1

            next_up_floor = now_floor + U
            next_down_floor = now_floor - D

            if 1 <= next_up_floor <= F and not visited[next_up_floor]:
                visited[next_up_floor] = True
                q.append((count, next_up_floor))
            if 1 <= next_down_floor <= F and not visited[next_down_floor]:
                visited[next_down_floor] = True
                q.append((count, next_down_floor))

    return "use the stairs"

if __name__ == "__main__":
    F, S, G, U, D = list(map(int, input().split()))

    print(count_button(F, S, G, U, D))