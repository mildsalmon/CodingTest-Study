# n, m = list(map(int, input().split()))
ice = []
result = 0

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

for i in range(n):
    ice.append(list(map(int, z[i])))


def dfs(x, y, depth, name='main'):
    print("x, y, way, 깊이 =", x, y, name, depth)
    depth = depth + 1
    if x >= 0 and x < n and y >= 0 and y < m:
        if ice[x][y] == 0:
            ice[x][y] = 1
            print(*ice, sep='\n')
            dfs(x, y-1, depth, name='서')
            dfs(x+1, y, depth, name='남')
            dfs(x, y+1, depth, name='동')
            dfs(x-1, y, depth, name='북')

            return True
        else:
            return False
    else:
        return False


for j in range(n):
    for k in range(m):
        if dfs(j, k, 1) == True:
            result = result + 1

print(result)