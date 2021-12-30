"""
Date    : 2021.12.30
Update  : 2021.12.30
Source  : 1261.py
Purpose : 다익스트라 / BFS
url     : https://www.acmicpc.net/problem/1261
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def dijkstra(start, graph) -> int:
    import heapq

    global n, m

    ds = ((1, 0), (0, 1), (-1, 0), (0, -1))

    visited = [[False] * m for _ in range(n)]

    q = []
    # (벽을 부순 횟수, x, y)
    heapq.heappush(q, (0, start[0], start[1]))

    while q:
        break_wall, x, y = heapq.heappop(q)
        # 만약 방문한 위치라면 continue
        if not visited[x][y]:
            if x == n - 1 and y == m - 1:
                break

            visited[x][y] = True
            # 상,하,좌,우 4방향 탐색
            for d in ds:
                dx = x + d[0]
                dy = y + d[1]

                if 0 <= dx < n and 0 <= dy < m:
                    # 방문하지 않은 위치만 q에 집어넣음
                    if not visited[dx][dy]:
                        if graph[dx][dy] == 1:
                            heapq.heappush(q, (break_wall + 1, dx, dy))
                        else:
                            heapq.heappush(q, (break_wall, dx, dy))

    return break_wall

def bfs(start, graph) -> int:
    from collections import deque

    global n, m

    ds = ((1, 0), (0, 1), (-1, 0), (0, -1))

    distance = [[-1] * m for _ in range(n)]
    distance[0][0] = 0

    q = deque()
    q.append((start[0], start[1]))

    while q:
        x, y = q.popleft()

        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx < n and 0 <= dy < m:
                # 방문하지 않은 곳이라면,
                if distance[dx][dy] == -1:
                    # 벽이라면,
                    if graph[dx][dy] == 1:
                        q.append((dx, dy))
                        distance[dx][dy] = distance[x][y] + 1
                    # 벽이 아니라면,
                    else:
                        q.appendleft((dx, dy))
                        distance[dx][dy] = distance[x][y]

    return distance[n-1][m-1]


if __name__ == "__main__":
    m, n = list(map(int, input().split()))
    graph = []

    for i in range(n):
        temp = list(map(int, input()))
        graph.append(temp)

    print(bfs(start=(0,0), graph=graph))
