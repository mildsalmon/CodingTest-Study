"""
Date    : 2022.01.15
Update  : 2022.01.15
Source  : 5014.py
Purpose : bfs
url     : https://www.acmicpc.net/problem/5014
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys
from collections import deque

input = sys.stdin.readline

def bfs(S: int, G: int) -> str:
    global F, U, D

    init_count = 0

    q = deque()
    q.append((init_count, S))

    visited = [False] * (F+1)

    if check(S, G, U, D):
        while q:
            count, floor = q.popleft()

            if floor == G:
                return str(count)

            count += 1

            down = floor - D
            up = floor + U

            # floor는 검증이 끝난 값이므로,
            # down의 경우 1층 이하로 떨어지는지, up의 경우 F층 이상으로 올라가는지만 확인해도 됨.
            # q에들어간 것은 이미 갔다고 체크해야 추후에 중복된 값이 들어가지 않음.
            if 1 <= down and not visited[down]:
                q.append((count, down))
                visited[down] = True
            if up <= F and not visited[up]:
                q.append((count, up))
                visited[up] = True

    return "use the stairs"

def check(S: int, G: int, U: int, D: int) -> bool:
    if (G - S < 0 and D == 0) or (G - S > 0 and U == 0):
        return False
    return True

if __name__ == "__main__":
    F, S, G, U, D = list(map(int, input().split()))

    print(bfs(S, G))
