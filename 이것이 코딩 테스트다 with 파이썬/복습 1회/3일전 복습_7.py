# Ch6_정렬_성적이 낮은 순서로 학생 출력하기

# N명의 학생 정보
# 학생 정보 = 이름, 성적
# 성적이 낮은 순서로 출력

# Input
# 학생 수 N (10만)
# N+1줄까지 [학생 이름 성적] (문자열의 길이와 성적은 100이하 자연수)

# nlogn, n, logn

# Output
# 성적이 낮은 순서로 이름 출력 / 한줄로

# n = int(input())
# array = []
# for i in range(n):
#     name, score = list(input().split())
#     array.append([name, int(score)])
#
# array.sort(key=lambda x: x[1])
#
# for i in array:
#     print(i[0], end=' ')

# Ch6_정렬_두 배열의 원소 교체

# 두 배열 A, B
# 두 배열은 N개의 원소로 구성
# 배열의 원소는 모두 자연수
# 최대 K번 배열 A, B의 원소를 바꿔치기 가능
# 목표는 배열 A의 모든 원소의 합이 최대가 되는 것.

# Input
# N, K가 공백으로 구분되어 입력 (N은 10만, K는 10만)
#   O(nlogn) = 170만, O(n) = 10만, O(logn) = 17
# 배열 A의 원소들이 공백으로 구분 (원소는 1000만보다 작음)
# 배열 B의 원소들이 공백으로 구분 (원소는 1000만보다 작음)

# Output
# 배열 A의 원소의 합의 최댓값

n, k = list(map(int, input().split()))
A = []
B = []

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

for i in range(k):
    for j in range(n):
        if B[j] > A[i]:
            A[i], B[j] = B[j], A[i]

print(sum(A))

# nlog(n) + O(k * n) => 170만 + 100억

### 시간 복잡도 초과

A.sort()
B.sort(reverse=True)

for i in range(k):
    if B[i] > A[i]:
        A[i], B[i] = B[i], A[i]

# 2nlog(n) + O(k) => 340만 + 10만