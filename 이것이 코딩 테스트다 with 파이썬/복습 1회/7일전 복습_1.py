# Ch3_그리디_큰수의법칙

# M = 총 더하는 횟수
# K = 연속해서 더할 수 있는 횟수

# 단순한 풀이

# n, m, k = list(map(int, input().split()))
# A = list(map(int, input().split()))
#
# A.sort(reverse=True)
#
# first = A[0]
# second = A[1]
#
# result = 0
#
# for i in range(m):
#     if i % (k+1) == 0:
#         result = result + second
#     else:
#         result = result + first
#
# print(result)

# 공식 유추

# result = 0
#
# result = (m//(k+1))*(first * k + second) + (m % (k+1))*first
#
# print(result)

# ---------------------------------------------

# Ch3_그리디_숫자카드게임

# 가장 높은 숫자가 쓰인 카드 한장 뽑기
# 카드가 N*M 형태로 있음
# 행에서 제일 작은 카드를 뽑고 그 중에서 제일 큰 수를 출력

# n, m = list(map(int, input().split()))
# array = []
#
# for i in range(n):
#     a = list(map(int, input().split()))
#     array.append(min(a))
#
# print(max(array))

# ---------------------------------------------

# Ch3_그리디_1이 될 때까지

# N이 1이 될 떄까지 반복
# N - 1
# N // K => N이 K로 나누어 떨어질 때만
# 반복하는 횟수 출력

# n, k = list(map(int, input().split()))
#
# count = 0
#
# while n != 1:
#     if n % k == 0:
#         n = n // k
#     else:
#         n = n - 1
#     count = count + 1
#
# print(count)

# Ch4_구현_상하좌우

# n = int(input())
# array = list(input())
#
# d_string = ("L", "R", "U", "D")
# ds = [(0, -1),
#       (0, 1),
#       (-1, 0),
#       (1, 0)]
#
# x, y = 1, 1
#
# for i in array:
#     for j, d in enumerate(d_string):
#         if d == i:
#             dx = x + ds[j][0]
#             dy = y + ds[j][1]
#
#             if dx <= 0 or dx > 5 or dy <= 0 or dy > 5:
#                 continue
#             else:
#                 x = dx
#                 y = dy
#
# print(x, y)
#
# x, y = 1, 1
#
# for i in array:
#     for j in range(len(d_string)):
#         if i == d_string[j]:
#             dx = x + ds[j][0]
#             dy = y + ds[j][1]
#
#             if dx <= 0 or dx > 5 or dy <= 0 or dy > 5:
#                 continue
#             else:
#                 x = dx
#                 y = dy
#
# print(x, y)

# Ch4_구현_시각

# 정수 N
# 00시 00분 00초 ~ N시 59분 59초 중 3이 하나라도 포함된 경우의 수

n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)
            if "3" in time:
                count = count + 1
                # print(time)

print(count)