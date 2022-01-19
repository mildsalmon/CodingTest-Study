n = int(input())
array = list(map(int, input().split()))

if n == 1:
    print(array[0])
else:
    array.sort()

    if n % 2 == 0:
        half = n // 2 - 1
    elif n % 2 == 1:
        half = n // 2
    total = 1e9
    answer = half
    for i in range(half, half+2):
        temp_total = 0
        for j in range(n):
            temp_total += abs(array[i] - array[j])
        if temp_total < total:
            answer = i
            total = temp_total

    print(array[answer])