# # 특정 거리의 도시 찾기
#
# from collections import deque
#
# n, m, k, x = list(map(int, input().split()))
#
# array = [[] for i in range(n+1)]
#
# for i in range(m):
#     temp = list(map(int, input().split()))
#
#     array[temp[0]].append(temp[1])
#
# q = deque()
# q.append(x)
#
# distance = [k+1 for i in range(n+1)]
# distance[x] = 0
#
# while q:
#     src = q.popleft()
#
#     for i in array[src]:
#         cost = distance[src] + 1
#         if cost < distance[i]:
#             distance[i] = cost
#             q.append(i)
#
# answer = []
#
# for i in range(1, n+1):
#     if distance[i] == k:
#         answer.append(i)
#
# if len(answer) == 0:
#     print(-1)
# else:
#     answer.sort()
#     print(*answer, sep='\n')

# 외벽 점검

from itertools import permutations


def solution(n, weak, dist):
    weak_len = len(weak)

    for i in range(weak_len):
        weak.append(weak[i] + n)

    combi_dist = list(permutations(dist, len(dist)))

    answer = len(dist) + 1

    for start in range(weak_len):
        for friends in combi_dist:
            count = 1
            point = weak[start] + friends[0]
            for i in range(start, start + weak_len):
                if point < weak[i]:
                    count += 1
                    if count > len(dist):
                        break
                    point = weak[i] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1

    return answer

solution(12, [1, 5, 6, 10], [1, 2, 3, 4])