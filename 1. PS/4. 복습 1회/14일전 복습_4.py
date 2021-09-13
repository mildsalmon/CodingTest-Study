# Ch5_DFS/BFS_음료수 얼려 먹기

# NxM 크기의 얼음 틀
# 구멍이 뚫려 있는 부분은 0
# 칸막이는 1
# 구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
# 얼음 틀 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하라

# Input
    # 세로 길이 N, 가로 길이 M
        # 1 <= N, M <= 1,000
    # N+1줄까지 얼음 틀 형태
        # 구멍이 뚫린 부분은 0
        # 그렇지 않은 부분은 1

# Output
    # 한 번에 만들 수 있는 아이스크림 개수

def dfs(map_dfs, x, y):
    global n
    global m

    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if map_dfs[x][y] != 1:

        # print(*map, sep='\n')
        map_dfs[x][y] = 1

        dfs(map_dfs, x - 1, y)
        dfs(map_dfs, x + 1, y)
        dfs(map_dfs, x, y - 1)
        dfs(map_dfs, x, y + 1)

        return True
    return False

n, m = 15, 14
z =['00000111100000',
    '11111101111110',
    '11011101101110',
    '11011101100000',
    '11011111111111',
    '11011111111100',
    '11000000011111',
    '01111111111111',
    '00000000011111',
    '01111111111000',
    '00011111111000',
    '00000001111000',
    '11111111110011',
    '11100011111111',
    '11100011111111',]

# n, m = list(map(int, input().split()))
game_map = []
answer = 0

for i in range(n):
    game_map.append(list(map(int, z[i])))
    # game_map.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        if dfs(game_map, i, j) == True:
            answer += 1
            # print(*game_map, sep='\n')
print(answer)

# 23분 29초 / pass / 다 잘 풀었는데, 맵을 입력받는 부분에서 int로 안받아서 에러가 발생했다. 로직에는 문제가 없는거 같은데 하고 한참을 보니
# game_map.append(list(input())) 이더라. game_map.append(list(map(int, input())))으로 해야 정수형으로 입력받아지는건데.