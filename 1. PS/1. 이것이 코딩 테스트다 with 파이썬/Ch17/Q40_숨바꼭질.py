"""
Date    : 2021.11.26
Update  : 2021.11.26
Source  : Q40_숨바꼭질.py
Purpose : 다익스트라 알고리즘을 활용하여 1번 헛간에서 가장 멀리 있는 헛간을 구한다.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import heapq

# 헛간 수, 헛간 통로의 수
n, m = list(map(int, input().split()))

# 인접 리스트로 헛간 통로를 입력받음
graph = [[] for i in range(n+1)]

# 헛간은 양방향 통로가 존재한다고 명시되어 있으므로, A -> B, B -> A 모두 인접 리스트에 입력함.
for _ in range(m):
    start, end = list(map(int, input().split()))

    graph[start].append(end)
    graph[end].append(start)

# 최단거리를 업데이트하는 리스트를 만듬.
# 최단거리를 구하는 것이기 때문에, 초기값은 양의 무한대를 줌
distance = [1e9 for i in range(n+1)]
# 처음 시작하는 위치의 최단거리는 0으로 줌
distance[1] = 0

# 힙으로 사용할 q 생성
q = []
# q에는 현재까지의 최단거리와 해당 노드 번호를 입력함.
heapq.heappush(q, (distance[1], 1))

while q:
    dist, node = heapq.heappop(q)

    # 현재까지의 최단거리가 최단거리 리스트에 있는 값보다 크다면, 최단거리가 아니므로 반복문의 시작으로 돌아감
    if dist > distance[node]:
        continue

    # 현재 노드와 연결된 노드들을 탐색
    for next_node in graph[node]:
        # 각 노드 사이의 거리는 무조건 1
        # 노드 사이의 거리를 비용으로 생각하지 않고, 횟수로 생각하기 때문.
        next_node_dist = 1
        cost = dist + next_node_dist

        # 현재 노드와 다음 노드의 비용(거리)를 더했을 때, 최단 거리보다 작다면 교체함.
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(q, (distance[next_node], next_node))

# 번호, 거리, 같은 거리 개수
result = [0, 0, 0]

for i in range(1, n+1):
    # distance를 node가 작은 순서대로 탐색하면서, 최단 거리가 긴 node를 발견하면 값(노드 번호, 거리, 같은 거리 횟수)을 전부 교체
    if result[1] < distance[i]:
        result = [i, distance[i], 1]
    # 최단 거리가 가장 긴 노드와 같은 최단 거리를 가지는 노드가 존재하면, 같은 거리 갯수를 증가.
    elif result[1] == distance[i]:
        result[2] += 1

print(*result, sep=' ')