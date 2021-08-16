from collections import deque

# n, m = list(map(int, input().split()))
miro = []
miro_2 = []
n, m = [5, 6]
v = ['101010',
    '111111',
    '000001',
    '111111',
    '111111']

for i in range(n):
    a = list(map(int, v[i]))
    miro.append(a[:])
    miro_2.append(a[:])

roots = deque()
roots.append([0, 0])

d = [(0, -1), (1, 0), (0, 1), (-1, 0)]

while roots:
    x, y = roots.popleft()
    miro_2[x][y] = 0
    count = 0

    for j in range(4):
        dx = x + d[j][0]
        dy = y + d[j][1]

        if dx < 0 or dx >= n or dy < 0 or dy >= m:
            continue

        if miro[dx][dy] == 0:
            continue

        if miro[dx][dy] == 1 and miro_2[dx][dy] != 0:
            roots.append([dx, dy])
            miro[dx][dy] = miro[x][y] + 1
            count = count + 1
        elif miro[dx][dy] >= 1:
            count = count + 1
    if count <= 1:
        if x == 0 and y == 0:
            miro[x][y] = 1
        else:
            miro[x][y] = 0

    print(x,y)
    print(*miro, sep='\n')
    print()
    print(*miro_2, sep='\n')

    if miro[n-1][m-1] != 1:
        break

print(miro[n-1][m-1])

###########################################
############ 결과 값 #######################
# 10
#
# map
# [1, 0, 0, 0, 0, 0]
# [2, 3, 4, 5, 6, 7]
# [0, 0, 0, 0, 0, 8]
# [1, 1, 1, 1, 10, 9]
# [1, 1, 1, 1, 1, 10]
