from itertools import combinations

def dfs(array, x, y, d):
    global n
    # teacher가 탐색한다.
    # 탐색해서 학생을 찾으면 true
    dx = x + d[0]
    dy = y + d[1]

    if 0 <= dx < n and 0 <= dy < n:
        if array[dx][dy] == 'X':
            answer = dfs(array, dx, dy, d)
        elif array[dx][dy] == 'S':
            return True
        else:
            return False
    else:
        return False

    return answer

global array, student, teacher, no_exist, n

n = int(input())

array = []
student = []
teacher = []
no_exist = []

for i in range(n):
    temp = list(input().split())
    array.append(temp)
    for j in range(n):
        if temp[j] == 'S':
            student.append((i, j))
        elif temp[j] == 'T':
            teacher.append((i, j))
        elif temp[j] == 'X':
            no_exist.append((i, j))

def solution():
    global array, student, teacher, no_exist, n

    combi_no_exists = list(combinations(no_exist, 3))
    ds = ((0, -1), (1, 0), (0, 1), (-1, 0))

    for combi_no_exist in combi_no_exists:
        temp_array = [i[:] for i in array]
        answer = []
        for i in combi_no_exist:
            x, y = i
            temp_array[x][y] = 'O'

        for t in teacher:
            x, y = t
            search_d = []
            for d in ds:
                search_d.append(dfs(temp_array, x, y, d))
            if True in search_d:
                answer.append(True)
                break
        if True in answer:
            continue
        # 모든 학생이 감시로부터 피했다면
        return "YES"
    return "NO"

print(solution())