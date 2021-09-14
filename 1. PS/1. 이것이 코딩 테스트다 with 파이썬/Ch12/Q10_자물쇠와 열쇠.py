# def move(key, d_count):
#     d = [[0, len(key), 0, len(key)],
#          [0, len(key), len(key), 0],
#          [len(key), 0, len(key), 0],
#          [len(key), 0, 0, len(key)]]
#
#     new_key = [[0] * len(key) for i in range(len(key))]
#
#     for i in range(d[d_count][0], d[d_count][1]):
#         for j in range(d[d_count][2], d[d_count][3]):
#             if d_count % 2 == 0:
#                 new_key[i][j] = key[i][j]
#             elif d_count % 2 == 1:
#                 new_key[i][j] = key[j][i]
#     return new_key
#
#
# def solution(key, lock):
#     for l in range(4):
#         new_key = move(key, l)
#
#         for i in range(len(lock)):
#             for j in range(len(lock)):
#                 # for k in range(len(key)):
#                 if lock[i][j] == 0 and new_key[i][j] == 1:
#                     return True
#
#     return False

# def move_key(key):
#     # 키 행렬을 회전
#
#     row = len(key)
#     column = len(key[0])
#     new_key = [[0] * column for i in range(row)]
#
#     for i in range(row):
#         for j in range(column):
#             new_key[i][j] = key[(row - j) - 1][i]
#     # print(*new_key, sep='\n')
#     # print()
#     return new_key
#
#
# def solution(key, lock):
#     row = len(lock)
#     column = len(lock[0])
#     extend_lock = [[0] * column * 3 for i in range(row * 3)]
#
#     for i in range(row):
#         for j in range(column):
#             extend_lock[row + i][column + j] = lock[i][j]
#
#     for m in range(4):
#         # temp_extend_lock = [i[:] for i in extend_lock]
#         for i in range(row*2):
#             for j in range(column*2):
#                 count = 0
#                 sample_key = [i[:] for i in key]
#                 for k in range(len(key)):
#                     for l in range(len(key)):
#                         sample_key[k][l] += extend_lock[k+i][l+j]
#                 for k in range(len(key)):
#                     for l in range(len(key)):
#                         if sample_key[k][l] == 1:
#                             count += 1
#                 if count == 9:
#                     return True
#                 print(*sample_key, sep='\n')
#                 print()
#         key = move_key(key)
#
#     return False

def transform_key(key):
    m = len(key)
    new_key = [[0]*m for i in range(m)]

    for i in range(m):
        for j in range(m):
            new_key[i][j] = key[m-j-1][i]
    # print(*new_key,sep='\n')
    return new_key

def solution(key, lock):
    m = len(key)
    n = len(lock)

    new_lock = [[0]*n*3 for _ in range(n*3)]

    for i in range(n, n*2):
        for j in range(n, n*2):
            new_lock[i][j] = lock[i%n][j%n]

    # print(*new_lock, sep='\n')

    for _ in range(4):
        key = transform_key(key)
        for i in range(n*2+1):
            for j in range(n*2+1):
                # 열쇠 삽입
                for k in range(m):
                    for l in range(m):
                        new_lock[i+k][j+l] += key[k][l]
                # 잠금 해제되는지 체크
                count = 0
                for k in range(n, 2*n):
                    for l in range(n, 2*n):
                        if new_lock[k][l] == 1:
                            count += 1
                if count == n*n:
                    return True
                # 열쇠 뽑기 + 잠금장치 원위치
                for k in range(m):
                    for l in range(m):
                        new_lock[i+k][j+l] -= key[k][l]
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))