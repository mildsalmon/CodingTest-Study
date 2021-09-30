# Ch7_이진탐색_부품찾기

# 부품 N개 있다.
# 각 부품은 정수 형태의 고유 번호가 있다.
# 손님이 M개 종류의 부품을 대량 구매하겠다고 한다.
# M개 종류를 모두 확인해서 견적서를 작성해야 한다.

# Input
    # N
        # 1 <= N <= 1,000,000
    # N개의 정수가 주어진다.
    # M
        # 1 <= M <= 100,000
    # M개의 정수가 주어진다.

# Output
    # 각 부품이 존재하면 yes, 아니면 no

n = int(input())
A = list(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))

A.sort()

for i in B:
    if i in A:
        print('yes', end=' ')
    else:
        print('no', end=' ')