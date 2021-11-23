# 도시의 개수
n = int(input())
# 버스의 개수
m = int(input())

# 모든 도시의 인접행렬
array = [[1e9] * n for _ in range(n)]

# 대각 행렬 초기화
for i in range(n):
    array[i][i] = 0

# 버스 정보 입력
for i in range(m):
    src_city, dest_city, cost = list(map(int, input().split()))

    array[src_city-1][dest_city-1] = min(cost, array[src_city-1][dest_city-1])

# i -> j 까지 가는데 최소 비용 구함 (플로이드로)
for k in range(n):
    for i in range(n):
        for j in range(n):
            array[i][j] = min(array[i][k] + array[k][j], array[i][j])

# 만약 i -> j로 갈 수 없다면 0으로 출력
for i in range(n):
    for j in range(n):
        if array[i][j] == 1e9:
            array[i][j] = 0

        print(array[i][j], end=' ')
    print()

# print(*array, sep='\n')
