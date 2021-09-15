# # Ch10_그래프 이론_커리큘럼
#
# from collections import deque
#
# n = int(input())
#
# graph = [[] for i in range(n+1)]
# time = [0] * (n+1)
# indegree = [0] * (n+1)
#
# for i in range(1, n+1):
#     temp = list(map(int, input().split()))
#     time[i] = temp[0]
#
#     for j in temp[1:-1]:
#         graph[j].append(i)
#         indegree[i] += 1
# # print(time)
# result_time = time[:]
# q = deque()
# q.append((result_time[1], 1))
# # print(result_time)
# for i in range(len(graph)):
#     now_time, now_node = q.popleft()
#
#     for j in graph[now_node]:
#         next_time = time[j]
#         next_node = j
#
#         if next_time > result_time[j]:
#             continue
#
#         result_time[j] = max(next_time+now_time, result_time[j])
#         q.append((result_time[j], next_node))
#         indegree[i] -= 1
#
# print(*result_time[1:], sep='\n')
#
# # 5
# # 10 -1
# # 10 1 -1
# # 4 1 -1
# # 4 3 1 -1
# # 3 3 -1
#
# # 22분

# # Ch11_그리디_Q1 모험가 길드
#
# n = int(input())
# array = list(map(int, input().split()))
#
# array.sort(reverse=True)
#
# x_count = array[0]
# count = 0
#
# for i in range(len(array)):
#     if x_count == i+1:
#         count += 1
#         x_count += array[i]
#
# print(count)
#
# # 반례
#
# # 5
# # 1 1 1 1 1
# #
# # 5
# # 4 4 4 4 4
# #
# # 5
# # 1 2 4 3 1
# #
# # 5
# # 2 3 1 2 2

# 6분 21초