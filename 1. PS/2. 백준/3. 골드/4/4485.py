"""
Date    : 2021.12.29
Update  : 2021.12.29
Source  : 4485.py
Purpose :
url     : https://www.acmicpc.net/problem/4485
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import heapq

def make_adjacency_list(graph) -> list:
    global n

    dp = [[] for _ in range(n * n)]

        # 오른쪽, 아래, 왼쪽, 위
    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

    for i in range(n):
        for j in range(n):
            for d in ds:
                dx = i + d[0]
                dy = j + d[1]

                if 0 <= dx < n and 0 <= dy < n:
                    # (비용, x, y)
                    dp[(i*n)+j].append((graph[dx][dy], dx, dy))

    return dp

def make_distance(start) -> list:
    global n

    distance = [[1e9] * n for _ in range(n)]
    distance[start[0]][start[1]] = graph[start[0]][start[1]]

    return distance

def dijkstra(start, distance, dp) -> None:
    global n

    q = []
    heapq.heappush(q, (distance[start[0]][start[1]], start[0], start[1]))

    while q:
        cost, x, y = heapq.heappop(q)

        if distance[x][y] < cost:
            continue

        for next_cost, nx, ny in dp[(x*n)+y]:
            total_cost = cost + next_cost

            if distance[nx][ny] > total_cost:
                distance[nx][ny] = total_cost
                heapq.heappush(q, (total_cost, nx, ny))

def end_check(n):
    if n == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    tc = 0

    while True:
        n = int(input())

        if end_check(n):
            break
        else:
            tc += 1

        graph = []
        for _ in range(n):
            temp = list(map(int, input().split()))
            graph.append(temp)

        start = (0, 0)

        dp = make_adjacency_list(graph)

        distance = make_distance(start)

        dijkstra(start, distance, dp)

        # print(*distance, sep='\n')

        print(f"Problem {tc}: {distance[n-1][n-1]}")