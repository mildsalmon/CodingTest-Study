# Q10. 자물쇠와 열쇠

def transform(key):
    key_len = len(key)
    temp = [[0] * key_len for i in range(key_len)]
    for i in range(key_len):
        for j in range(key_len):
            temp[i][j] = key[key_len - j - 1][i]

    return temp

def solution(key, lock):
    lock_len = len(lock)
    key_len = len(key)

    big_lock = [[0]*3*lock_len for i in range(3*lock_len)]

    # print(*big_lock, sep='\n')

    for i in range(lock_len, 2*lock_len):
        for j in range(lock_len, 2*lock_len):
            big_lock[i][j] = lock[i-lock_len][j-lock_len]

    # print(*big_lock, sep='\n')

    for _ in range(4):
        for i in range(len(big_lock)-key_len):
            for j in range(len(big_lock)-key_len):
                # 자물쇠에 열쇠 넣음
                for k_i in range(key_len):
                    for k_j in range(key_len):
                        big_lock[i+k_i][j+k_j] += key[k_i][k_j]

                # 올바른 키인지 확인
                count = 0
                for c_i in range(lock_len, 2*lock_len):
                    for c_j in range(lock_len, 2*lock_len):
                        if big_lock[c_i][c_j] == 1:
                            count += 1
                if count == (lock_len * lock_len):
                    return True
                # print(*big_lock, sep='\n')
                # print()
                # 올바른 키가 아니기 때문에 좌물쇠에서 열쇠 뺌
                for k_i in range(key_len):
                    for k_j in range(key_len):
                        big_lock[i+k_i][j+k_j] -= key[k_i][k_j]
        key = transform(key)
        # print(*key, sep='\n')
        # print()
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# 34분 / pass