"""
Date    : 2022.02.25
Update  : 2022.02.25
Source  : 9370.py
Purpose : 다익스트라
url     : https://www.acmicpc.net/problem/9370
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys
import heapq

input = sys.stdin.readline


def dijkstra(start: int, distance: list, value: int) -> None:
    global graph

    q = []
    heapq.heappush(q, (value, start))
    distance[start] = value

    while q:
        cost, node = heapq.heappop(q)

        if cost > distance[node]:
            continue

        for next_cost, next_node in graph[node]:
            total_cost = cost + next_cost

            if total_cost < distance[next_node]:
                distance[next_node] = total_cost
                heapq.heappush(q, (total_cost, next_node))

if __name__ == "__main__":
    for tc in range(int(input())):
        n, m, t = list(map(int, input().split()))
        s, g, h = list(map(int, input().split()))

        graph = [[] for _ in range(n+1)]
        distance = [1e9 for _ in range(n+1)]

        for _ in range(m):
            a, b, d = list(map(int, input().split()))

            graph[a].append((d, b))
            graph[b].append((d, a))

        dijkstra(s, distance, 0)

        g_distance = [1e9 for _ in range(n+1)]
        h_distance = [1e9 for _ in range(n+1)]

        dijkstra(g, g_distance, distance[g])
        dijkstra(h, h_distance, distance[h])

        # destination_candidate = []

        for _ in range(t):
            x = int(input())
            # destination_candidate.append(x)
            # print(distance)
            # print(g_distance)
            # print(h_distance)
            if distance[x] == g_distance[x] == h_distance[x]:
                print(x, end=' ')