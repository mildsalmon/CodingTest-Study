# n개의 도시가 있다.
# 각 도시는 보내고자 하는 메시지가 있는 경우, 다른 도시로 전보를 보내서 다른 도시로 해당 메시지를 전송할 수 있다.
# X -> Y로 전보를 보내려면 X에서 Y로 향하는 통로가 설치되어 있어야 한다. => 단방향

# C라는 도시에서 메시지를 보내려고 한다.
# 메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나간다.
# 각 도시의 번호와 통로 정보가 주어졌을때,
# 도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇개
# 모두 메시지를 받는데 걸리는 시간을 얼마인가

# Input
    # n, m, c = 도시의 개수, 통로의 개수, 메시지를 보내고자 하는 도시
    # M+1줄까지 통로에 대한 정보 x,y,z
        # 특정 도시 x에서 y로 이어지는 통로가 있고, 전달 시간이 z임.

# Output
    # 첫째줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 걸리는 시간.

import heapq

INF = int(1e9)

n, m, c = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
# distance[c] = 0


for i in range(m):
    a, b, z = list(map(int, input().split()))

    graph[a].append((b, z))

# print(*graph, sep='\n')

def dijkstra(start):
    q = []
    # print(start)
    # print(graph[start])
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # distance[0] = 0
    count = 0
    while q:
        c, b = heapq.heappop(q)

        if distance[b] < c:
            continue

        for i in graph[b]:
            cost = c + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                count = count + 1
            # if i[1] < distance[b]:
            #     distance[b] = i[1]
            #     count = count + 1
            #     heapq.heappush(b, distance[b])
    return count

count = dijkstra(c)
print(distance)
print(count, end=' ')
print(max(distance))