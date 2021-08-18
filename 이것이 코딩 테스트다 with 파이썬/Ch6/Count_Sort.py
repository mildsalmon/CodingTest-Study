array = [7, 5, 6, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2, 99, 150]

count = [0] * (max(array) + 1)

for i in array:
    count[i] = count[i] + 1

print("count = ", count)

print("sorted = ", end='')
for j in range(len(count)):
    for k in range(count[j]):
        print(j, end=' ')