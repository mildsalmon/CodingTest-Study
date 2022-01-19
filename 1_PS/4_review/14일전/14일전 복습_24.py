# 자물쇠와 열쇠

def transpose_key(key):
    new_key = []
    for k in zip(*key):
        new_key.append(k)
    new_key.reverse()
    return new_key


def check_lock(big_lock, lock_len):
    for x in range(lock_len, 2 * lock_len):
        for y in range(lock_len, 2 * lock_len):
            if big_lock[x][y] != 1:
                return False
    return True


def solution(key, lock):
    key_len = len(key)
    lock_len = len(lock)

    big_lock = [[0] * lock_len * 3 for i in range(lock_len * 3)]

    for i in range(lock_len, 2 * lock_len):
        for j in range(lock_len, 2 * lock_len):
            big_lock[i][j] = lock[i - lock_len][j - lock_len]

    # print(*big_lock,sep='\n')

    for _ in range(4):
        key = transpose_key(key)

        # print(*key, sep='\n')
        # print()

        for i in range(2 * lock_len):
            for j in range(2 * lock_len):
                for x in range(key_len):
                    for y in range(key_len):
                        big_lock[i + x][j + y] += key[x][y]

                if check_lock(big_lock, lock_len):
                    return True

                for x in range(key_len):
                    for y in range(key_len):
                        big_lock[i + x][j + y] -= key[x][y]
                # print(*big_lock,sep='\n')
    return False