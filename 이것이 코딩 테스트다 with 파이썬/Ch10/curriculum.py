# from collections import deque
#
# n = int(input())
#
# indegree = [0] * (n+1)
# total_time = [0] * (n+1)
# graph = [[] for _ in range(n+1)]
#
# for i in range(1, n+1):
#     array = list(map(int, input().split()))
#     time = array[0]
#
#     for j in range(1, len(array)):
#         if array[j] == -1:
#             pass
#             # total_time[i] += time
#         else:
#             graph[array[j]].append([i, time])
#             indegree[i] += 1
#         total_time[i] += time
# q = deque()
# q.append([1, 0])
#
# while q:
#     next_subject, time = q.popleft()
#     indegree[next_subject] -= 1
#
#     if indegree[next_subject] == 0:
#         total_time[next_subject] += time
#
from collections import deque

n = int(input())

indegree = [0] * (n+1)
time = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    array = list(map(int, input().split()))
    time[i] = array[0]

    for j in array[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

q = deque()
result_time = time[:]

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
print('inde', indegree)
while q:
    node = q.popleft()
    print('node', node)
    print('result', result_time)
    print('time  ', time)
    for i in graph[node]:
        print('i', i)
        result_time[i] = max(result_time[i], result_time[node]+time[i])

        indegree[i] -= 1
        print('inde', indegree)
        if(indegree[i] == 0):
            q.append(i)



for i in result_time[1:]:
    print(i)

# 57분 / non-pass / 위상 정렬을 구현하는 방법을 잘 이해하지 못함.