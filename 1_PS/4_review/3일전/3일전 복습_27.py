# Q13.  배달

from itertools import combinations

n, m = list(map(int, input().split()))

house = []
chicken = []

for i in range(n):
    temp = list(map(int, input().split()))
    # 치킨, 집 좌표를 따로 리스트에 담음
    for j in range(len(temp)):
        if temp[j] == 1:
            house.append([i, j])
        elif temp[j] == 2:
            chicken.append([i, j])

combi_chicken = []
# 치킨 조합
for i in range(1, m+1):
    for j in list(combinations(chicken, i)):
        combi_chicken.append(j)
        # print(j)
# 치킨 조합 잘 나오는지 확인인
# print(*combi_chicken, sep='\n')

answer = 1e9
for c_c in combi_chicken:
    sum_distance = 0
    for h in house:
        distance = 1e9
        for c in c_c:
            distance = min(abs(h[0] - c[0]) + abs(h[1] - c[1]), distance)
        sum_distance += distance
    # print(sum_distance)
    answer = min(answer, sum_distance)

print(answer)

# 28분 / Pass