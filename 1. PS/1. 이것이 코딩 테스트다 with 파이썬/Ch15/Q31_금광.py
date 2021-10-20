T = int(input())
col_row = []
array = [[] for i in range(T)]

for j in range(T):
    row, col = list(map(int, input().split()))

    col_row.append((row, col))

    temp = list(map(int, input().split()))

    for i in range(row):
        array[j].append(temp[i*col:(i*col)+col])

    # print(array)

# dp = [0] * T
#
# for i, a in enumerate(array):
#     for z in zip(*a):
#         dp[i] += max(z)
#         print(z)
# print(dp)

dp = []
answer = []
for i, c_r in enumerate(col_row):
    row, col = c_r
    # print(row, col)
    dp.append([0] * row)
    # print(dp)
    # for i in dp[-1]:
    for r in range(row):
        dp[-1][r] = array[i][r][0]
        next_r_pos = r
        for c in range(1, col):
            next_r_value = 0
            # for j in range(3):
            if next_r_pos-1 >= 0:
                if next_r_value < array[i][next_r_pos-1][c]:
                    next_r_value = array[i][next_r_pos-1][c]
                    next_r_save = next_r_pos - 1
                # next_r = max(array[i][c][r-1], next_r)
            if next_r_pos+1 < row:
                if next_r_value < array[i][next_r_pos+1][c]:
                    next_r_value = array[i][next_r_pos+1][c]
                    next_r_save = next_r_pos + 1
                # next_r = max(array[i][c][r+1], next_r)
            if next_r_value < array[i][next_r_pos][c]:
                next_r_value = array[i][next_r_pos][c]
                next_r_save = next_r_pos
                # next_r = max(array[i][c][r], next_r)
            next_r_pos = next_r_save
            dp[-1][r] += next_r_value

    answer.append(max(dp[-1]))

print(*answer, sep='\n')

# 1시간 5분 56초


