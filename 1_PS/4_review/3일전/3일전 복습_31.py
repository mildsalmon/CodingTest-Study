def dfs(x, y, array, d):
    global N

    dx = x + d[0]
    dy = y + d[1]

    if 0 <= dx < N and 0 <= dy < N:
        if array[dx][dy] == 'X':
            result = dfs(dx, dy, array, d)

            return result
        # 장애물을 만나서 학생을 찾지 못했다.
        elif array[dx][dy] == 'O':
            return True
        # 학생을 찾았다.
        elif array[dx][dy] == 'S':
            return False
    # 범위를 벗어나서 학생을 찾지 못했다.
    return True

def recursive(count, array):
    global N, teacher
    # 장애물 3개 설치 완료
    if count == 3:
        ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

        for t in teacher:
            x, y = t
            for d in ds:
                result = dfs(x, y, array, d)
                # 학생을 발견했을 경우
                # 더 이상 탐색은 무의미하기 때문에, 장애물을 재배치함.
                if not result:
                    return False
        # 선생님이 모든 방향을 탐색했는데, 학생이 발견되지 않았을 경우
        return True
    # 장애물 3개 설치 미완료
    elif count != 3:
        for i in range(N):
            for j in range(N):
                # 장애물도 학생도 없는 칸이라면,
                # 장애물을 설치할 수 있다면.
                if array[i][j] == 'X':
                    count += 1
                    array[i][j] = 'O'

                    answer = recursive(count, array)

                    if answer:
                        return True

                    array[i][j] = 'X'
                    count -= 1
        return False

global N, teacher

N = int(input())

array = []
teacher = []

for i in range(N):
    temp = list(input().split())
    array.append(temp)

    for j in range(len(temp)):
        if temp[j] == 'T':
            teacher.append((i, j))

answer = recursive(0, array)

if answer:
    print("YES")
else:
    print("NO")