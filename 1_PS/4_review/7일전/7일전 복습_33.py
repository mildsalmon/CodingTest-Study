# 블록 이동하기

from collections import deque


def solution(board):
    q = deque()
    # x1, y1, x2, y2, time
    q.append((0, 0, 0, 1, 0))

    moved = set()
    moved.add((0, 0, 0, 1))

    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

    n = len(board)

    while q:
        x1, y1, x2, y2, time = q.popleft()

        if (x1 == n - 1 and y1 == n - 1) or (x2 == n - 1 and y2 == n - 1):
            return time

        for d in ds:
            dx1 = x1 + d[0]
            dy1 = y1 + d[1]
            dx2 = x2 + d[0]
            dy2 = y2 + d[1]

            if 0 <= dx1 < n and 0 <= dy1 < n and 0 <= dx2 < n and 0 <= dy2 < n:
                if board[dx1][dy1] == 0 and board[dx2][dy2] == 0:
                    if (dx1, dy1, dx2, dy2) not in moved:
                        q.append((dx1, dy1, dx2, dy2, time + 1))
                        moved.add((dx1, dy1, dx2, dy2))

        for i in (-1, 1):
            # 가로 -> 세로 변환
            if x1 == x2:
                dx1 = x1 + i
                dy1 = y1
                dx2 = x2 + i
                dy2 = y2

                if 0 <= dx1 < n and 0 <= dy1 < n and 0 <= dx2 < n and 0 <= dy2 < n:
                    if board[dx1][dy1] == 0 and board[dx2][dy2] == 0:
                        if (x2 + i, y2, x2, y2) not in moved:
                            q.append((x2 + i, y2, x2, y2, time + 1))
                            moved.add((x2 + i, y2, x2, y2))

                        if (x1, y1, x1 + i, y1) not in moved:
                            q.append((x1, y1, x1 + i, y1, time + 1))
                            moved.add((x1, y1, x1 + i, y1))

            # 세로 -> 가로 변환
            elif y1 == y2:
                dx1 = x1
                dy1 = y1 + i
                dx2 = x2
                dy2 = y2 + i

                if 0 <= dx1 < n and 0 <= dy1 < n and 0 <= dx2 < n and 0 <= dy2 < n:
                    if board[dx1][dy1] == 0 and board[dx2][dy2] == 0:
                        if (x1, y1 + i, x1, y1) not in moved:
                            q.append((x1, y1 + i, x1, y1, time + 1))
                            moved.add((x1, y1 + i, x1, y1))

                        if (x2, y2, x2, y2 + i) not in moved:
                            q.append((x2, y2, x2, y2 + i, time + 1))
                            moved.add((x2, y2, x2, y2 + i))

