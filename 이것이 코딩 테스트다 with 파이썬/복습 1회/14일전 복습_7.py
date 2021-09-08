# # Ch6_정렬_성적 낮은 순서로 학생 출력하기
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

# Ch6_정렬_두 배열의 원소 교체

n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]

print(sum(A))