n = int(input())

array = list()
array.append(1)

num = [2, 3, 5]

for i in range(1000):
    temp = [array[i] * j for j in num]

    array += temp
    array = set(array)
    array = list(array)
    array.sort()

print(array[n-1])

##########################################

n = int(input())

array = list()
array.append(1)

num = [2, 3, 5]

for i in range(n):
    temp = [array[i] * j for j in num]

    array += temp
    array = set(array)
    array = list(array)
    array.sort()

print(array[n-1])