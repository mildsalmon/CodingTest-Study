n = int(input())
num = []
array = []
for i in range(n):
    A = list(input().split())
    num.append(int(A[0]))
    array.append(A[1])
# print(num)
for i in range(len(array)):
    for j in array[i]:
        print(j*num[i], end='')
    print()