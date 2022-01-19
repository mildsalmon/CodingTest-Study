def check_matrix(matrix):
    start_w_check = 0
    start_b_check = 0
    for i in range(8):
        for j in range(8):
            di = i%2
            dj = j%2
            # 0번째가 W일 때
            if (di == 0 and dj == 0) or (di == 1 and dj == 1):
                if matrix[i][j] == "W":
                    start_w_check += 1
                elif matrix[i][j] == "B":
                    start_b_check += 1
            elif (di == 0 and dj == 1) or (di == 1 and dj == 0):
                if matrix[i][j] == "B":
                    start_w_check += 1
                elif matrix[i][j] == "W":
                    start_b_check += 1
    result = max(start_w_check, start_b_check)
    # print(start_w_check, start_b_check)
    # print(result)
    return (8*8)-result

n, m = list(map(int, input().split()))
array = []

for i in range(n):
    array.append(list(input()))

check = ["W", "B"]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
check_map = [[0] * m for _ in range(n)]
answer = []

n_i = n - 7
m_j = m - 7
# print(n_i, m_j)
for i in range(n_i):
    for j in range(m_j):
        sample_matrix = [row[j:j+8] for row in array[i:i+8]]
        # print(*sample_matrix, sep='\n')
        answer.append(check_matrix(sample_matrix))

print(min(answer))