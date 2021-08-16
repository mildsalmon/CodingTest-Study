# n, m = list(map(int, input().split()))
# a, b, d = list(map(int, input().split()))
n, m = 4, 4
a, b, d = 1, 1, 0
v = ["1 1 1 1",
     "1 0 0 1",
     "1 1 0 1",
     "1 1 1 1"]

game_map = []
d_all = [(-1, 0), (0, 1), (1, 0), (0, -1)]
count = 0

for i in range(n):
    game_map.append(list(map(int, v[i].split(" "))))

def move(x, y, d, depth=0):
    global count
    print("x, y, d, count, depth", x, y, d, count, depth)
    depth = depth + 1
    if x >= 0 and x < n and y >= 0 and y < m:
        if game_map[x][y] == 0:
            game_map[x][y] = 1
            print(*game_map, sep='\n')
            count = count + 1
            for j in d_all:
                dx = x - d_all[d][0]
                dy = y - d_all[d][1]

                d = d + 1

                if d % 4 == 0:
                    d = d - 4

                move(dx, dy, d, depth)
            return count
        else:
            return False
    else:
        return False

count = move(a,b, d)

print(count)