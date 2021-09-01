# # Ch3_그리디_큰 수의 법칙
#
# # 배열에 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# # 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번 초과하여 더해질 수 없다.
#
# # Input
#     # N, M, K
#         # N (2 <= N <= 1000)
#         # M (1 <= M <= 10000)
#         # K (1 <= K <= 10000)
#     # N개의 자연수
#         # 1 <= a <= 10000
#
# # Output
#     # 큰수의 법칙에 따라 더해진 답을 출력
#
# n, m, k = list(map(int, input().split()))
# array = list(map(int, input().split()))
#
# array.sort()
#
# a = array[-1]
# b = array[-2]
# result = 0
#
# for i in range(m):
#     if i % (k+1) == 0:
#         result = result + b
#     else:
#         result = result + a
#
# print(result)

# # Ch3_그리디_숫자 카드 게임
#
# # NxM 형태로 카드가 놓여짐, N은 행, M은 열
# # 먼저 뽑고자 하는 카드가 포함된 행을 선택
# # 행에서 숫자가 낮은거 선택
# # 최종적으로 가장 높은거 선택
#
# # Input
#     # N, M
#         # 1 <= N, M, 100
#     # N개 줄에 걸쳐 숫자가 주어진다.
#         # 1이상 10000 이하
#
# # Output
#     # 룰에 맞는 카드 선택
#
# n, m = list(map(int, input().split()))
# array = []
#
# for i in range(n):
#     a = (list(map(int, input().split())))
#     array.append(min(a))
#
# print(max(array))

# # Ch3_그리디_1이 될 때까지
#
# # N이 1이 될 때까지 아래 과정을 반복적으로 선택하여 수행
# # 두 번째 연산은 N이 K로 나누어질 때만 선택
#     # N = N - 1
#     # N = N // K
#
# # Input
#     # N, K
#         # N (2 <= N <= 100000)
#         # K (2 <= K <= 100000)
#
# n, k = list(map(int, input().split()))
# count = 0
#
# while n != 1:
#     if n % k == 0:
#         n = n // k
#     else:
#         n = n - 1
#
#     count = count + 1
#
# print(count)

# # Ch4_구현_상하좌우
#
# # 여행가 A는 NxN 크기의 정사각형 공간에 있다.
# # 가장 왼쪽 좌표는 1, 1
# # 가장 오른쪽 좌표는 N, N
# # A는 상하좌우 방향만 이동
# # 이동 계획
#
# # InpiDara
#     # 움직일 정사각형 NxN 선택
# # Outdata
#     # 1 <= 이동 횟수 <= 100
#
# n = int(input())
# array = list(input().split())
#
# d = ('L', "R", "U", "D")
# distance = ((0, -1), (0, 1), (-1, 0), (1, 0))
#
# x = 1
# y = 1
#
# for i in array:
#     for j in range(len(d)):
#         if d[j] == i:
#             dx = x + distance[j][0]
#             dy = y + distance[j][1]
#
#             if dx <= 0 or dx > n or dy <= 0 or dy > n:
#                 continue
#
#             x = dx
#             y = dy
#
# print(x, y)

# Ch4_구현_시각

# 정수 N이 입력,
# 00시 00분 00초부터 N시 59분 59초까지 3이 하나라도 포함되면 카운트

n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)
            if '3' in time:
                count = count + 1

print(count)