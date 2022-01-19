# # Ch10_그래프이론_커리큘럼
#
# from collections import deque
#
# n = int(input())
# graph = [[] for _ in range(n+1)]
# # time = []
# time = [0] * (n+1)
# indegree = [0] * (n+1)
#
# for i in range(1, n+1):
#     A = list(map(int, input().split()))
#     # time.append(A[0])
#     time[i] = A[0]
#     for j in A[1:-1]:
#         graph[j].append(i)
#         indegree[i] += 1
#
# result_time = time[:]
# q = deque()
#
# for i in range(1, n+1):
#     if indegree[i] == 0:
#         q.append(i)
#
# # for i in range(1, n+1):
# while q:
#     i = q.popleft()
#     for j in graph[i]:
#         result_time[j] = max(result_time[j], result_time[i]+time[j])
#         indegree[j] -= 1
#
#         if indegree[j] == 0:
#             q.append(i)
#
# print(*result_time[1:], sep='\n')
#
# # 25분 53초

# Ch11_그리디_모험가 길드

n = int(input())
array = list(map(int, input().split()))

array.sort(reverse=True)
end = array[0]
group = 1
for i in range(n):
    if i == end:
        if end + array[i] <= n:
            end = end + array[i]
            group += 1
        # print(end)
print(group)

# 12분 44초
