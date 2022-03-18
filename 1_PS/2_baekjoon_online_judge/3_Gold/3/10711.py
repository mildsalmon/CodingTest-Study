"""
Date    : 2022.03.18
Update  : 2022.03.18
Source  : 10711.py
Purpose : bfs
url     : https://www.acmicpc.net/problem/10711
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
from collections import deque


def wave(castles, sands):
    global h, w

    ds = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

    q = deque()
    q.append(castles)
    time = 0

    while q:
        castles = q.popleft()
        temp_sands = [sands[i][:] for i in range(h)]
        temp_castles = []

        for cx, cy in castles:
            cnt = 0
            for d in ds:
                dx = cx + d[0]
                dy = cy + d[1]

                if sands[dx][dy] == '.':
                    cnt += 1
            if cnt >= sands[cx][cy]:
                temp_sands[cx][cy] = '.'
            else:
                temp_castles.append((cx, cy))

        if castles[:] == temp_castles[:]:
            break
        time += 1
        sands = [temp_sands[i][:] for i in range(h)]
        q.append(temp_castles)

    return time

if __name__ == "__main__":
    h, w = list(map(int, input().split()))
    sands = []
    castles = []

    for i in range(h):
        temp = list(input())
        for j in range(w):
            if temp[j] != '.':
                castles.append((i, j))
                temp[j] = int(temp[j])
        sands.append(temp)

    print(wave(castles, sands))