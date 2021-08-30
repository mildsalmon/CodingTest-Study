# Ch6_정렬_위에서 아래로

# 수열을 큰수부터 작은 수의 순서로 정렬하라
# 내림차순

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

# array.sort(reverse=True)
# print(array)

array.sort()

print(array[::-1])