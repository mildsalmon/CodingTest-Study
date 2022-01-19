# 배열 A의 합이 최대
# 배열 A와 배열 B를 최대 K번 바꿀 수 있음.
# A, B는 N개의 원소로 구성
# 최악의 경우 N = 100,000 / K = 100,000
# nlogn, n, logn
# 계수 정렬 X

# n, k = list(map(int, input().split()))
# A = []
# B = []
#
# for i in input().split():
#     A.append(int(i))
#
#
# for i in input().split():
#     B.append(int(i))
#
# A.sort()
# B.sort(reverse=True)
#
# for i in range(k):
#     if A[i] < B[i]:
#         A[i], B[i] = B[i], A[i]
#
# print(sum(A))

# ---------------------------------

# 성적 낮은 순서로 이름 출력
# nlogn, n

# n = int(input())
# array = []
#
# for i in range(n):
#     name, score = list(input().split())
#     array.append([name, int(score)])
#
# result = sorted(array, key=lambda x: x[1])
#
# for i in result:
#     print(i[0], end=' ')
