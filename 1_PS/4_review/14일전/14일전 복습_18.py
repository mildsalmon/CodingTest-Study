from collections import deque

n = int(input())

lecture = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
time = [0] * (n+1)

for i in range(1, n+1):
    temp = list(map(int, input().split()))
    time[i] = temp[0]

    for j in range(1, len(temp)):
        if temp[j] == -1:
            break
        lecture[temp[j]].append(i)
        indegree[i] += 1

answer = time[:]
q = deque()

for i in range(len(indegree)):
    if indegree[i] == 0:
        q.append(i)

while q:
    node = q.popleft()

    for next_node in lecture[node]:
        sum_time = answer[node] + time[next_node]
        answer[next_node] = max(answer[next_node], sum_time)

        indegree[next_node] -= 1

        if indegree[next_node] == 0:
            q.append(next_node)

print(*answer[1:], sep='\n')
print()

# 28분 / pass