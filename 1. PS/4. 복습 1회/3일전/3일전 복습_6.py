# Ch6_정렬_위에서 아래로 문제

# 수열의 수를 큰 수부터 작은 수의 순서로 정렬

# Input
# 수열의 개수 N (최악의 경우 500)
# 둘째줄부터 N+1번째 줄까지 N개의 수가 입력됨. (수의 범위는 10만 이하 자연수)

# Output
# 수열을 내림차순으로 정렬

n = int(input())
array = []

for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

print(*array, sep=' ')