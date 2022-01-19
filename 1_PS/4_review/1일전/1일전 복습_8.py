# Ch7_이진탐색_부품 찾기 문제

# 부품 N개 있다.
# 각 부품은 정수 형태의 고유 번호가 있다.
# M개 종류의 부품을 구매하는 손님이 있다.
# 부품 M개 종류을 모두 확인해야 한다.

# Input
# N, 매장 부품 번호, M, 손님 요청 부품 번호

# Output
# 손님이 요청한 부품 번호의 순서대로 확인하여 있으면 yes, 없으면 no

# N은 최악의 경우 100만 => nlogn => 2000만, logn => 20, n => 100만
# M은 최악의 경우 10만 => nlogn => 170만, logn => 17, n => 10만

n = 5
A = "8 3 7 9 2"
m = 3
B = "5 7 9"

# O(m) => 10만

# n = int(input())

store_parts = list(map(int, A.split()))
# store_parts = list(map(int, input().split()))

# m = int(input())
customer_parts = list(map(int, B.split()))
# customer_parts = list(map(int, input().split()))

result = []

for i in customer_parts:
    if i in store_parts:
        result.append("yes")
    else:
        result.append("no")

print(*result, sep=' ')

del customer_parts
del store_parts
del result

# O(n) => 계수 정렬을 이용한 탐색

# n = int(input())
store_parts = [0 for __ in range(1000001)]
for i in list(map(int, A.split())):
# for i in list(input()):
    store_parts[i] = 1

# m = int(input())
customer_parts = list(map(int, B.split()))
# customer_parts = list(map(int, input().split()))

result = []

for i in customer_parts:
    if store_parts[i] == 1:
        result.append("yes")
    else:
        result.append("no")

print(*result, sep=' ')

del customer_parts
del store_parts
del result

## 계수 정렬 2탄 = 딕셔너리 사용하여 메모리 낭비 방지

store_parts = {}
for i in list(map(int, A.split())):
    store_parts[i] = 1

customer_parts = list(map(int, B.split()))

result = []

for i in customer_parts:
    if i in store_parts.keys():
        result.append("yes")
    else:
        result.append("no")

print(*result, sep=' ')

del customer_parts
del store_parts
del result

# O(logn) => 이진 탐색을 이용.

# def binary_search():


store_parts = list(map(int, A.split()))
customer_parts = list(map(int, B.split()))

result = []

store_parts.sort()

for i in customer_parts:
    start = 0
    end = n - 1
    while(start <= end):
        mid = (start + end) // 2
        if store_parts[mid] == i:
            result.append("yes")
            break
        if i < store_parts[mid]:
            end = mid - 1
        elif i > store_parts[mid]:
            start = mid + 1
    if i != store_parts[mid]:
        result.append('no')

print(*result, sep=' ')

