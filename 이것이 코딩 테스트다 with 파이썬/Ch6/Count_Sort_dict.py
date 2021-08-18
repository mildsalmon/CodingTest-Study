array = [7, 5, 6, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2, 99, 150]

count = dict()

for i in array:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1

count = sorted(count.items(), key=lambda x:x[0])

print("count = ", count)

print("sorted = ", end='')
for i_key, i_value in count:
    for j in range(i_value):
        print(i_key, end=' ')

