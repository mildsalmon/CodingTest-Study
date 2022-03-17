"""
Date    : 2022.03.17
Update  : 2022.03.17
Source  : 4179.py
Purpose :
url     : https://www.acmicpc.net/problem/4179
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
from collections import deque


def move(q: deque) -> int:
    global miro

    ds = ((1, 0), (0, 1), (-1, 0), (0, -1))

    while q:
        # 불 -> 지훈 이동
        x, y, time, fires = q.popleft()

        temp = set()

        for fx, fy in fires:
            for d in ds:
                fdx = fx + d[0]
                fdy = fy + d[1]

                if 0 <= fdx < r and 0 <= fdy < c:
                    if miro[fdx][fdy] == '#':
                        continue

                    temp.add((fdx, fdy))
        fires = fires.union(temp)

        # 지훈
        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx < r and 0 <= dy < c:
                if (dx, dy) in fires or miro[dx][dy] == '#':
                    continue

                q.append((dx, dy, time+1, fires))
            else:
                return time+1
        # print(*miro, sep='\n')
        # print(q)
        # print()
    return -1


if __name__ == "__main__":
    r, c = list(map(int, input().split()))
    miro = []
    pos = []
    fires = set()

    for i in range(r):
        temp = list(input())
        miro.append(temp)

        for j in range(c):
            if temp[j] == 'J':
                pos = [i, j, 0]
            elif temp[j] == 'F':
                fires.add((i, j))
    pos.append(fires)

    q = deque()
    q.append(pos)

    time = move(q)

    if time == -1:
        print("IMPOSSIBLE")
    else:
        print(time)