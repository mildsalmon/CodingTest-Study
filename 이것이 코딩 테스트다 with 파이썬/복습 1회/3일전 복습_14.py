# # Ch9_최단 경로_미래 도시
#
# # 방문 판매원 A는 미래 도시에 있다.
# # 미래 도시에는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어 있다.
# # A는 1번 회사에 있으며, X번 회사에 방문해 물건을 판매하고자 한다.
# # 특정 회사에 도착하기 위한 방법은 회사끼리 연결되어 있는 도로를 이용하는 방법이 유일하다.
# # 연결된 2개의 회사는 양방향으로 이동할 수 있다.
# # 도로 이동에는 1만큼의 시간이 든다.
#
# # 소개팅 상대는 K번 회사에 있다.
# # A(1번회사)는 K번 회사에 방문하고 X번 회사에 방문하려한다.
# # 가능한 빠르게 이동하는 최소 시간을 계산하라.
#
# # 소개팅 소요시간은 고려하지 않는다.
#
# # Input
#     # 회사 개수 N, 경로의 개수 M
#         # 1 <= N, M <= 100
#     # M+1번째 줄까지 연결된 두 회사 정보
#     # M+2번째 줄에는 X와 K
#         # 1 <= K <= 100
#
# # Output
#     # A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간
#     # X번 회사에 도달할 수 없다면 -1
#
# n, m = list(map(int, input().split()))
# INF = int(1e9)
# company = [[INF] * (n+1) for _ in range(n+1)]
#
# for i in range(n+1):
#     for j in range(n+1):
#         if i == j:
#             company[i][j] = 0
#
# for i in range(m):
#     a, b = map(int, input().split())
#     company[a][b] = 1
#     company[b][a] = 1
#
# x, k = list(map(int, input().split()))
#
# # 반복문이 1부터 시작해야 헛도는걸 방지할 수 있음.
# # 없어도 크게 문제는 안되나, 무의미한 시간 복잡도가 증가함.
# # for z in range(1, n+1):
# #     for a in range(1, n+1):
# #         for b in range(1, n+1):
# #             company[a][b] = min(company[a][b], company[a][z] + company[z][b])
#
# for z in range(n+1):
#     for a in range(n+1):
#         for b in range(n+1):
#             company[a][b] = min(company[a][b], company[a][z] + company[z][b])
#
# # print(*company, sep='\n')
#
# answer = company[1][k] + company[k][x]
#
# if answer >= INF:
#     print(-1)
# else:
#     print(answer)
#
# # 22분 3초 / Pass
# # 두번째 복습이라 플로이드 워셜 알고리즘으로 풀었지만, 다음부터는 다익스트라로 풀어보자.

# Ch9_최단 경로_전보

# N개의 도시가 있다.
# 메시지를 다른 도시로 전보를 보내서 메시지를 전송할 수 있다.
# X -> Y = X에서 Y로 향하는 통로가 설치되어 있어야 한다.
# X에서 Y로 향하는 통로 O, Y에서 X로 향하는 통로 X면 Y는 X로 메시지 보낼 수 없다.
# 통로를 거쳐 메시지 보낼때는 일정 시간이 소요된다.

# C 도시에 위급 상황 발생
# 최대한 많은 도시로 메시지 전달하려 한다.
# 도시 C에서 보낸 메시지를 받게 되는 도시의 개수와 도시들이 모두 메시지를 받는 데 걸리는 시간을 구하라.

# Input
    # 도시의 개수 N, 통로의 개수 M, 메시지 보내고자하는 도시 C
        # 1 <= N <= 30,000
        # 1 <= M <= 200,000
        # 1 <= C <= N
    # M+1 줄까지 통로에 대한 정보 X, Y, Z
        # 특정 도시 X에서 Y 도시로 이어지는 통로의 전달 시간 Z
        # 1 <= X, Y <= N
        # 1 <= Z <= 1,000

import heapq

def dijkstra(citys, distance, start):
    q = []
    heapq.heappush(q, (0, start))
    count = 0
    while q:
        pop_cost, pop_city = heapq.heappop(q)

        # 이거 추가 안했음.(실수) 테스트 케이스가 많았다면 에러 발생할 수도 있었음.
        # if distance[pop_city] < pop_cost:
        #     continue

        for city in citys[pop_city]:
            city_cost, city_destination = city
            accumulate_cost = city_cost + pop_cost

            if distance[city_destination] > accumulate_cost:
                distance[city_destination] = accumulate_cost
                heapq.heappush(q, (accumulate_cost, city_destination))
                count += 1

    return count

n, m, c = list(map(int, input().split()))

citys = [[] for _ in range(n+1)]

for i in range(m):
    x, y, z = list(map(int, input().split()))
    citys[x].append((z, y))

INF = int(1e9)
distance = [INF] * (n+1)
distance[c] = 0

count = dijkstra(citys, distance, c)
total_time = max(distance[1:])

print(distance)
print(count, total_time)

# 31분 26초 / Pass
# 다음에는 플로이드 워셜로 해보자.
# 실전에서는 시간 복잡도를 초과하기 때문에 불합이 뜨겠지만, 이건 다양한 알고리즘을 적용하는 연습이니까.