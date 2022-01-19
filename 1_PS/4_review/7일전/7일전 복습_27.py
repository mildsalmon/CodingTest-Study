# 치킨 배달

from itertools import combinations

N, M = list(map(int, input().split()))
array = []
houses = []
chickens = []

for i in range(N):
    temp = list(map(int, input().split()))

    array.append(temp)
    for j in range(len(temp)):
        if temp[j] == 1:
            houses.append((i, j))
        elif temp[j] == 2:
            chickens.append((i, j))

combination_chickens = combinations(chickens, M)

min_town_chicken_distance = 1e9
# 치킨집 조합에서 하나를 선택
for chickens in combination_chickens:
    town_chicken_distance = 0
    # 집들 중 하나 선택
    # 각 집과 조합에서 선택된 치킨집 사이의 가장 가까운 치킨 거리 계산
    for house in houses:
        min_chicken_distance = 1e9
        for chicken in chickens:
            chicken_distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            min_chicken_distance = min(min_chicken_distance, chicken_distance)
        # 구한 치킨 거리를 도시의 치킨 거리에 더함.
        town_chicken_distance += min_chicken_distance
    min_town_chicken_distance = min(min_town_chicken_distance, town_chicken_distance)

print(min_town_chicken_distance)