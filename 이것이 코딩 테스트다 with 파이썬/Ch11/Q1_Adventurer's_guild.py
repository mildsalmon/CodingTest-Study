# n = int(input())
# arrays = list(map(int, input().split()))

# A = sorted(arrays)
# arrays.sort(reverse=True)

# trips = []

# while arrays:
#     trip = []
#     i = A.pop()
#     for j in range(i):
#         trip.append(arrays[j])
#     del arrays[:j+1]
#     trips.append(trip)
#
# print(len(trips))

# top_pick = []
# top_pick.append(arrays[0])
# for i in range(len(arrays)):
#     if top_pick[-1] == i:
#         top_pick.append(arrays[i])
#         if sum(top_pick) > len(arrays):
#             del top_pick[-1]
#             break
#
# print(len(top_pick))

# start = 0
# end = 0
# interval = 0
#
# for i in range(len(arrays)):
#     if end == i:
#         start = i
#         end = arrays[i] + i
#         interval = arrays[i]
#         if len(arrays) < (len(trips) + interval):
#             break
#         else:
#             trips.append(arrays[start:end])
#
#         print(trips)
#         print(sum(trips))
# print(len(trips))

import time

start = time.time()

# n = int(input())
# arrays = list(map(int, input().split()))
n = 5
# arrays = [1, 1, 1, 1, 1]
# arrays = [4, 4, 4, 4, 4]
arrays = [3, 2, 2, 2, 1]

arrays.sort(reverse=True)
group = 0
start = 0
i = 0
while arrays:
    if start == i:
        start = arrays[0]
        if len(arrays) >= start:
            group += 1
            i = 0
    else:
        pass
    arrays.pop(0)
    i += 1
print(group)

end = time.time()

print(end-start)
# 1시간 25분 25초 / pass / timeout /
# 풀다가 풀다가 내가 만든 테스트 케이스를 통과하지 못해서 답지 코드를 봤다.
# 그런데 답지 코드도 내가 만든 테스트 케이스에서 틀린 답을 준다.
# 그래서 내가 생각한 테스트 케이스에서도 잘 동작하는 코드를 만드는데 시간이 조금 걸렸다.

# 테스트 케이스
# (Input => Output)
#
# 5 / 1 1 1 1 1 => 5
# 5 / 4 4 4 4 4 => 1
# 5 / 1 2 4 3 1 => 2
# 5 / 2 3 1 2 2 => 2

start = time.time()

# n = int(input())
# arrays = list(map(int, input().split()))
n = 5
# arrays = [1, 1, 1, 1, 1]
# arrays = [4, 4, 4, 4, 4]
arrays = [3, 2, 2, 2, 1]

arrays.sort(reverse=True)
group = 0
start = 0
count = 0
ar = []
del_array = []
for i in range(len(arrays)):
    if start == count:
        start = arrays[i]
        ar.append(start)
        if len(arrays) - len(del_array) >= start:
            group += 1
            count = 0
    del_array.append(arrays[i])
    count += 1

print(group)

end = time.time()

print(end-start)
# 시간 복잡도 개선판.
# 첫 번째 코드는 pop(i)로 인해 시간복잡도가 O(N^2)이 된다. (while문 N * pop(i) N)
# 따라서 밑에 코드처럼 작성하면 시간복잡도가 O(N)이 된다. (append는 O(1)이므로)

# time 함수로 시간을 찍어보면서 몇 번 돌려봤는데, 테스트케이스의 길이가 작아서 그런지, 소요 시간이 완전히 똑같이 나온다.