from collections import deque

# n, m = list(map(int, input().split()))
miro_map = []
miro_map_2 = []

n, m = [5, 6]
v = ['101010',
    '111111',
    '000001',
    '111111',
    '111111']

for i in range(n):
    a = list(map(int, v[i]))
    miro_map.append(a[:])
    miro_map_2.append(a[:])


start_point = [0, 0]
end_point = [n-1, m-1]

moves = deque()
moves.append(start_point)

d = ((0, -1), (1, 0), (0, 1), (-1, 0))
result = 0

while moves:
    # count = count + 1
    print("moves :", moves)
    move = moves.popleft()
    print(move)
    count = 0
    x = move[0]
    y = move[1]
    result = result + 1
    miro_map_2[x][y] = 0

    print(*miro_map, sep='\n')
    print("miro_2\n", *miro_map_2, sep='\n')

    for j in range(4):
        dx = x + d[j][0]
        dy = y + d[j][1]
        if dx >= 0 and dx < n and dy >= 0 and dy < m:
            if miro_map_2[dx][dy] == 1:
                count = count + 1
                moves.append([dx, dy])
                miro_map[x][y] = result

            # else:
    if count < 1:
        result = result - 1
    print("result :", result)

print(result)