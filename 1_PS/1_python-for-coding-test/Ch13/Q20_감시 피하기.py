def dfs(x, y, graph, d):
    global n

    if 0 <= x < n and 0 <= y < n:
        if graph[x][y] == 'X':
            dx = x + d[0]
            dy = y + d[1]

            result = dfs(dx, dy, graph, d)
            return result

        elif graph[x][y] == 'O':
            return False
        elif graph[x][y] == 'S':
            return True
    return False

def recursive(graph, count):
    global n, teacher, student, ds

    if count == 3:
        result = []
        for t in teacher:
            for d in ds:
                dx = t[0] + d[0]
                dy = t[1] + d[1]

                result.append(dfs(dx, dy, graph, d))

        if True not in result:
            return 'YES'
        else:
            return 'NO'

        # for i in range(n):
        #     for j in range(n):
        #         if graph[i][j] == 'T':
        #
    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    count += 1
                    graph[i][j] = 'O'
                    answer = recursive(graph, count)
                    if answer == 'YES':
                        return 'YES'
                    count -= 1
                    graph[i][j] = 'X'
        return 'NO'

global n, teacher, student, ds

n = int(input())

student = []
teacher = []

graph = []

ds = ((1, 0), (-1, 0), (0, 1), (0, -1))

for i in range(n):
    temp = list(input().split())
    graph.append(temp)
    for j in range(len(temp)):
        if temp[j] == "S":
            student.append([i, j])
        elif temp[j] == "T":
            teacher.append([i, j])

# print(*student, sep='\n')
# print()
# print(*teacher, sep='\n')
# print(*graph, sep='\n')

answer = recursive(graph, 0)

print(answer)

# 31분 / Pass

# 이전에 풀었던 문제(연구소)랑 비슷한 유형인 것 같아서 그냥 풀었다.
# 2차원 리스트를 3단계 재귀로 진입하는 문제 !
# 조합을 썻으면 더 편하게 풀었을지도 모르겠다
