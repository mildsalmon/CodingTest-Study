# 블록 이동하기

from collections import deque

def check_condition(board, lx, ly, rx, ry):
    global n

    if 0 <= lx < n and 0 <= ly < n and 0 <= rx < n and 0 <= ry < n:
        if board[lx][ly] == 0 and board[rx][ry] == 0:
            return True
    return False


def solution(board):
    global n

    n = len(board)

    q = deque()
    # lx, ly, rx, ry, time
    q.append((0, 0, 0, 1, 0))

    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))
    check = set()

    while q:
        lx, ly, rx, ry, time = q.popleft()

        for d in ds:
            d_lx = lx + d[0]
            d_ly = ly + d[1]
            d_rx = rx + d[0]
            d_ry = ry + d[1]

            if check_condition(board, d_lx, d_ly, d_rx, d_ry):
                if (d_lx, d_ly, d_rx, d_ry) not in check:
                    check.add((d_lx, d_ly, d_rx, d_ry))
                    q.append((d_lx, d_ly, d_rx, d_ry, time + 1))

                    if (d_lx == n - 1 and d_ly == n - 1) or (d_rx == n - 1 and d_ry == n - 1):
                        return time + 1

        if lx == rx:
            for i in [-1, 1]:
                d_lx = lx + i
                d_ly = ly
                d_rx = rx + i
                d_ry = ry

                if check_condition(board, d_lx, d_ly, d_rx, d_ry):
                    if (lx, ly, lx + i, ly) not in check:
                        check.add((lx, ly, lx + i, ly))
                        q.append((lx, ly, lx + i, ly, time + 1))

                        if (lx == n - 1 and ly == n - 1) or (lx + i == n - 1 and ly == n - 1):
                            return time + 1

                    if (rx + i, ry, rx, ry) not in check:
                        check.add((rx + i, ry, rx, ry))
                        q.append((rx, ry, rx + i, ry, time + 1))

                        if (rx == n - 1 and ry == n - 1) or (rx + i == n - 1 and ry == n - 1):
                            return time + 1

        if ly == ry:
            for i in [-1, 1]:
                d_lx = lx
                d_ly = ly + i
                d_rx = rx
                d_ry = ry + i

                if check_condition(board, d_lx, d_ly, d_rx, d_ry):
                    if (rx, ry + i, rx, ry) not in check:
                        check.add((rx, ry + i, rx, ry))
                        q.append((rx, ry + i, rx, ry, time + 1))

                        if (rx == n - 1 and ry + i == n - 1) or (rx == n - 1 and ry == n - 1):
                            return time + 1

                    if (lx, ly, lx, ly + i) not in check:
                        check.add((lx, ly, lx, ly + i))
                        q.append((lx, ly, lx, ly + i, time + 1))

                        if (lx == n - 1 and ly == n - 1) or (lx == n - 1 and ly + i == n - 1):
                            return time + 1


solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])