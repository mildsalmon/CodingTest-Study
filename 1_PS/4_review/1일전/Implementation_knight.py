xy = input()

x = int(ord(xy[0]) - ord('a') + 1)
y = int(xy[1])

dx = [-2, -2, 2, 2, 1, -1, 1, -1]
dy = [-1, 1, -1, 1, 2, 2, -2, -2]

count = 0

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        count = count + 1
    else:
        continue
print(count)