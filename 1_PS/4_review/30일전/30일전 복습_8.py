n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A.sort()

answer = []

for i in B:
    start = 0
    end = len(A)
    check = False
    while start <= end:
        mid = (start + end) // 2

        if A[mid] == i:
            check = True
            break
        elif i < A[mid]:
            end = mid - 1
        elif A[mid] < i:
            start = mid + 1

    if check:
        answer.append('yes')
    else:
        answer.append('no')

print(*answer, sep=' ')