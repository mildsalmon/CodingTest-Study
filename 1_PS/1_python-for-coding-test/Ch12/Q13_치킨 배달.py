from itertools import combinations

n, m = list(map(int, input().split()))

# graph = [[0] * (n+1) for _ in range(n+1)]

city_chicken_distance = 1e9
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

# for i in range(1, m+1):
home = []
chicken = []
ch_dp = []

# 치킨집과 가정집 각각 리스트에 좌표 추출
for j in range(n):
    for k in range(n):
        if graph[j][k] == 1:
            home.append([j, k])
            ch_dp.append(1e9)
        elif graph[j][k] == 2:
            chicken.append([j, k])

# 1~m개 치킨집의 조합을 구하기.
choice = []
for i in range(1, m+1):
    a = list(combinations(chicken, i))
    for j in a:
        choice.append(j)

# for step in range(1, m+1):
#     for i in range(0, len(chicken)):
#         if (i+step) >
#         choice = chicken[:(i+step)%(len(chicken)+1)]

# 조합된 치킨집과 가정집 사이의 멘헤튼 거리를 측정하고 최솟값을 찾는다.
for i in choice:
    ch_dp_t = ch_dp[:]

    for j in range(len(home)):
        for k in i:
            ch_dp_t[j] = min(ch_dp_t[j], abs(home[j][0] - k[0]) + abs(home[j][1] - k[1]))
    city_chicken_distance = min(city_chicken_distance, sum(ch_dp_t))

print(city_chicken_distance)

# 48분 / pass / 치킨집을 조합안쓰고 하나씩 고르려다가 시간초과...