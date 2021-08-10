# 소요시간 : 18분

n = int(input())
plans = list(map(str, input().split()))

move = ['L', 'R', 'U', 'D']
move_xy = [(0,-1), (0, 1), (-1, 0), (1, 0)]

x = 1
y = 1

for plan in plans:
    for i in range(len(move)):
        if plan == move[i]:
            if x + move_xy[i][0] >= 1 and x + move_xy[i][0] <= 5 and y + move_xy[i][1] >= 1 and y + move_xy[i][1] <= 5:
            # if x + move_xy[i][0] >= 1 and x + move_xy[i][0] <= n and y + move_xy[i][1] >= 1 and y + move_xy[i][1] <= n: # 5를 n으로 안바꿈. 실수함.
                x = x + move_xy[i][0]
                y = y + move_xy[i][1]

print(x, y)