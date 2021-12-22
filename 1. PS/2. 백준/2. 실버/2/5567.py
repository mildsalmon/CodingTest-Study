"""
Date    : 2021.12.22
Update  : 2021.12.22
Source  : 5567.py
Purpose : 다익스트라가 떠올라서 다익스트라로 풀었다.
url     : https://www.acmicpc.net/problem/5567
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

# 다익스트라
# 최단거리
# 최단 거리가 2 이하인 경우만 구함 (친구, 친구의 친구)

import heapq

def dijkstra(start) -> list:
    """
    최단거리를 구하는 목적으로 작성됨
    :param start: 시작하는 노드
    :return: 최단거리 dp테이블
    """
    global n, graph

    # 친구들의 최단 거리를 저장하는 dp
    distance = [1e9] * (n + 1)
    # 상근이(나)의 최단 거리 초기화
    distance[start] = 0

    # 다익스트라 알고리즘에서는 보통 heap을 사용한다.
    # 우선순위가 높은 것부터 삭제해야지 불필요한 연산이 진행되지 않기 때문이다.
    # 하지만, graph 값으로 가지고 있는 것은 나와 친구인 node 번호만 가지고 있기 때문에 우선순위를 매길 것이 없다.
    # 따라서, 단순 list로 구현해도 충분했을 것 같다.
    q = []
    heapq.heappush(q, (1, 0))

    while q:
        # 우선순위가 가장 높은 node pop
        node, cost = heapq.heappop(q)
        # 저장된 현재 node의 최단 거리가 pop한 cost(최단거리)보다 작다면 continue
        if distance[node] < cost:
            continue
        # graph의 현재 node와 연결된 다른 node들을 탐색
        for next_node in graph[node]:
            # 최단 거리는 현재 node의 최단 거리 + 1로 증가한다.
            next_cost = cost + 1
            # 저장된 다음 node의 최단 거리가 next_cost보다 크다면 최단거리 갱신 및 heap에 추가
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(q, (next_node, next_cost))

    return distance

def check_friend(distance) -> int:
    """
    친구, 친구의 친구를 판별하는 목적
    :param distance: 친구들 사이의 최단 거리(친구, 친구의 친구, 친구의 친구의 친구 ...)
    :return: 친구, 친구의 친구의 수
    """
    count = 0
    # 최단 거리가 2 이하인 경우만 구함.
    # 친구 = 1, 친구의 친구 = 2
    for i in range(2, len(distance)):
        if distance[i] <= 2:
            count += 1

    return count

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [[] for i in range(n+1)]

    for i in range(m):
        a, b = list(map(int, input().split()))
        # 주어진 친구를 graph로 입력받는다.
        graph[a].append(b)
        # 이 부분에서 A-B가 친구이면 B-A도 친구인 것을 인지했어야 한다.
        graph[b].append(a)

    distance = dijkstra(1)

    print(check_friend(distance))
