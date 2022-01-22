"""
Date    : 2022.01.22
Update  : 2022.01.22
Source  : 6. 스타트링크.py
Purpose :
url     : https://www.acmicpc.net/problem/5014
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

from collections import deque

def push_btn(f, s, g, u, d):
    min_push_btn = 1e9

    q = deque()
    q.append((s, 0))

    visited = set()
    visited.add(s)

    while q:
        floor, count = q.popleft()

        if floor == g:
            min_push_btn = min(min_push_btn, count)
            return str(min_push_btn)

        up = floor + u

        if up not in visited:
            if up <= f:
                visited.add(up)
                q.append((up, count+1))

        down = floor - d

        if down not in visited:
            if down >= 1:
                visited.add(down)
                q.append((down, count+1))

    if min_push_btn == 1e9:
        return "use the stairs"
    else:
        return str(min_push_btn)



if __name__ == "__main__":
    f, s, g, u, d = list(map(int, input().split()))

    print(push_btn(f, s, g, u, d))