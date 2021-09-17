# # Ch12_구현_문자열 압축

# def solution(s):
#     len_s = len(s)
#
#     for i in range(1, (len(s)//2)+1):
#         # 문자열을 자르는 단위를 표현
#         # 전체 문자열 길이의 절반 이상으로 넘어가면 문자열 압축 불가능으로 len(s)//2 + 1을 마지노선으로 줌.
#         count = 1
#         answer = ''
#         pre = s[0:i]
#         for j in range(i, len(s)+i, i):
#             # 현재 문자열이 이전 문자열과 다를때까지 반복
#             # 위에서 지정한 단위 만큼 문자열을 슬라이싱
#             now = s[j:j+i]
#
#             if pre == now:
#                 # 이전 문자열과 현재 문자열이 같다면
#                 count += 1
#             else:
#                 if count == 1:
#                     answer += pre
#                 elif count > 1:
#                     answer += str(count) + pre
#                 count = 1
#             pre = now
#         # 단위별로 압축한 문자열이 나옴
#         len_s = min(len_s, len(answer))
#         print(answer)
#
#     return len_s
#
# print(solution("ababcdcdababcdcd"))

# # 25분 51초

# Ch12_구현_자물쇠와 열쇠

def transform(key):
    key_len = len(key)
    new_key = [[0] * key_len for _ in range(key_len)]

    for i in range(key_len):
        for j in range(key_len):
            new_key[i][j] = key[key_len - j - 1][i]

    return new_key


def check(new_lock, lock_len):
    new_lock_len = len(new_lock)

    for k in range(new_lock_len):
        for l in range(new_lock_len):
            if k >= lock_len and k < 2 * lock_len and l >= lock_len and l < 2 * lock_len:
                if new_lock[k][l] != 1:
                    return False

    return True


def solution(key, lock):
    key_len = len(key)
    lock_len = len(lock)

    # lock 크기를 확대함 (lock_len * 3) * (lock_len * 3)
    new_lock = [[0] * (lock_len * 3) for _ in range(lock_len * 3)]

    for i in range(len(new_lock)):
        for j in range(len(new_lock[i])):
            if i >= lock_len and i < 2 * lock_len and j >= lock_len and j < 2 * lock_len:
                new_lock[i][j] = lock[i % lock_len][j % lock_len]
            # if i >= (lock_len - 1) and i < (2*lock_len - 1) and j >= (lock_len - 1) and j < (2*lock_len - 1):
            #     new_lock[i][j] = lock[]
    # print(*new_lock, sep='\n')

    for _ in range(4):
        for i in range(len(new_lock) - key_len + 1):
            for j in range(len(new_lock) - key_len + 1):
                # 키 삽입
                for k in range(key_len):
                    for l in range(key_len):
                        new_lock[k + i][l + j] += key[k][l]

                # 잠금 체크
                if check(new_lock, lock_len):
                    return True

                # 키 추출
                for k in range(key_len):
                    for l in range(key_len):
                        new_lock[k + i][l + j] -= key[k][l]

        key = transform(key)
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# 38분 / 73% / 100%
