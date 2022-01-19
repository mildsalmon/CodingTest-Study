# Ch5_BFS_미로 탈출

# n * m 크기의 직사각형 미로
# 초기 위치는 (1, 1)
# 출구는 (N, M)
# 한번에 한 칸씩 이동
# 괴물이 있는 부분은 0 / 없는 부분은 1

# 미로 탈출을 위한 최소 칸의 갯수는?
# 시작 칸과 마지막 칸을 모두 포함해서 계산

# Input
# n, m
    # 4 <= n, m <= 200
# 다음 n개 줄에 M개의 정수로 미로 정보가 제시됨
    # 수들은 공백 없이 붙어서 제공
    # 시작 칸과 마지막 칸은 항상 1

from collections import deque

n, m = list(map(int, input().split()))
array = []

for i in range(n):
    array.append(list(map(int, input())))

check = deque()
check.append([0, 0])

d = ((-1, 0),
     (1, 0),
     (0, -1),
     (0, 1))

while check:
    x, y = check.popleft()

    for i in range(4):
        dx = x - d[i][0]
        dy = y - d[i][1]

        if dx < 0 or dx >= n or dy < 0 or dy >= m:
            continue
        if array[dx][dy] == 1:
            check.append([dx, dy])
            array[dx][dy] = array[x][y] + 1
        else:
            continue

    if array[n-1][m-1] != 1:
        break
    # print(*array, sep='\n')
    # print()
    # print(check)
print(array[n-1][m-1])

# 성공 / 28분 34초
