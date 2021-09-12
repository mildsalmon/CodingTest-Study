# ch7_이진 탐색_부품 찾기

def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        else:
            if array[mid] < target:
                start = mid + 1
            elif target < array[mid]:
                end = mid - 1

            # binary_search(array, start, end, target)

    return -1

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A.sort()

for i in B:
    value = binary_search(A, 0, len(A), i)

    if value == -1:
        print("no", end=' ')
    else:
        print("yes", end=' ')