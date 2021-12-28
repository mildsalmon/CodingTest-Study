"""
Date    : 2021.12.28
Update  : 2021.12.28
Source  : 1916.py
Purpose : 다익스트라
url     : https://www.acmicpc.net/problem/1916
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import heapq

def dijkstra(start, destination):
    global n

    q = []
    heapq.heappush(q, (0, start))

    distance = [1e9] * (n + 1)
    distance[start] = 0

    while q:
        now_cost, now_node = heapq.heappop(q)

        if distance[now_node] < now_cost:
            continue

        for next_cost, next_node in citys[now_node]:
            total_cost = next_cost + now_cost

            if distance[next_node] > total_cost:
                distance[next_node] = total_cost
                heapq.heappush(q, (total_cost, next_node))

    return distance[destination]

if __name__ == "__main__":
    n = int(input())
    m = int(input())

    citys = [[] for i in range(n+1)]

    for i in range(m):
        a, b, cost = list(map(int, input().split()))

        citys[a].append((cost, b))

    src_node, dest_node = list(map(int, input().split()))

    print(dijkstra(src_node, dest_node))