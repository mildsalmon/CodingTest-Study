# Ch9_최단 경로_미래 도시

# 미래도시에는 1번부터 N번까지 회사가 있음
# 특정 회사끼리는 서로 도로를 통해 연결되어 있음.
# 방문 판매원 A는 현재 1번 회사에 위치하며, X번 회사에 방문해 문건을 판매하고자 함 => Dijkstra
# 회사끼리 연결되어 있는 도로를 이용하는 방법이 유일.
# 특정 회사와 다른 회사가 도로로 연결되어 있다면 1만큼의 시간이 소요

# 소개팅 상대는 K번 회사에 존재
# X번 회사에 가기 전에 K번 회사에 방문함. => 1번 -> K -> X

# 가능한 빠르게 이동하는 최소 시간을 계산하는 프로그램

# import heapq
#
# n, m = list(map(int, input().split()))
#
# array = [[] for i in range(n+1)]
# INF = int(1e9)
# distance = [0] * (n+1)
# q = []
#
# # for i in range(m):
# #     start, end = list(map(int,input().split()))
# #     array[start].append(end)
# #     distance.append(0)
#
# for i in range(m):
#     start, end = list(map(int, input().split()))
#     heapq.heappush(q, (1, start, end))
#
# x, k = list(map(int, input().split()))
#
# # for i in array:
# #     for j in i:
# #         heapq.push(q, (1, j))
#
# # for i in array:
# #     for j in i:
# #         if i == 1:
# #             distance[i][j] = 1
# #         else:
# #

# 1시간 / 실패

n, m = list(map(int, input().split()))
INF = int(1e9)
graph = [[INF] * (n+1) for i in range(n+1)]

for i in range(m):
    start, end = list(map(int, input().split()))
    graph[start][end] = 1
    graph[end][start] = 1

x, k = list(map(int, input().split()))

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for l in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            graph[start][end] = min(graph[start][end], graph[start][l] + graph[l][end])

result = graph[1][k] + graph[k][x]

if result >= INF:
    print(-1)
else:
    print(result)

print(*graph, sep='\n')

# 경유해서 가는 문제는 플로이드 워셜 알고리즘으로 풀어야하는데, 처음에 1에서 x로 방문한다를 보고 dijkstra라고 판단하여, 실수가 시작됨.