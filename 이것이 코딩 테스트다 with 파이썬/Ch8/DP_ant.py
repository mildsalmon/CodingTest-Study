n = int(input())
array = list(map(int, input().split()))

d = [0] * 101

for i in range(2, n):
    if i-3 < 0:
        array[i] = array[i-2] + array[i]
        continue

    A = array[i-2] + array[i]
    B = array[i-3] + array[i]

    array[i] = max(A, B)

print(array[-1])