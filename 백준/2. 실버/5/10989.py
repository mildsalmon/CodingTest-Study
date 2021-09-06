import sys

n = int(sys.stdin.readline())
# n = int(input())
array = [0] * 10001
for i in range(n):
    array[int(sys.stdin.readline())] += 1
    # array.append(int(input()))
# print(*array, sep='\n')
for i in range(1, len(array)):
    for j in range(array[i]):
        print(i)