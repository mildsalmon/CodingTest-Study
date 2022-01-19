# # Ch6_정렬_성적이 낮은 순서로 학생 출력하기
#
# # N명의 학생 정보가 있다.
#     # 학생 정보는 학생 이름과 성적으로 구분된다.
# # 성적이 낮은 순서대로 학생의 이름을 출력하라
#
# # Input
#     # 학생의 수 N
#         # 1 <= N <= 100,000 => nlogn : 2,000,000, n = 100,000, logn = 20
#     # N+1번째 줄까지 이름을 나타내는 문자열 A와 성적을 나타내는 정수 B가 입력된다
#         # 문자열 A의 길이와 성적은 100 이하의 자연수
#
# # Output
#     # 성적이 낮은 순서대로 이름을 출력한다.
#
# n = int(input())
# array = []
#
# for i in range(n):
#     name, score = list(input().split())
#     array.append((name, int(score)))
#
# array.sort(key=lambda x:x[1])
#
# for i in range(n):
#     print(array[i][0], end=' ')
#
# # 7분 / 성공

# ch6_정렬_두 배열의 원소 교체

# 배열 A, B가 있다.
    # 두 배열은 N개의 원소로 구성됨.
    # 배열의 원소는 모두 자연수
# 최대 K번 바꿔치기 연산을 수행.
    # 바꿔치기 = 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것
# 목표는 배열 A의 모든 원소 합이 최대가 되도록 하는 것

# Input
    # n, k
        # 1 <= n <= 100,000
        # 0 <= k <= n
    # 배열 A의 원소들이 공백으로 구분되어 입력
        # 모든 원소는 10,000,000보다 작은 자연수
    # 배열 B의 원소들이 공백으로 구분되어 입력
        # 모든 원소는 10,000,000보다 작은 자연수

# Output
    # 최대 K번 바꿔치기 연산을 수행하여 배열 A의 모든 원소의 합을 구하라

n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
    if B[i] > A[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))

# 7분 30초 / 성공