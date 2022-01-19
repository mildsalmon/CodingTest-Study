n = int(input())
array = list(map(int, input().split()))

max_score = max(array)

for i in range(len(array)):
    # if array[i] < max_score:
    array[i] = (array[i]/max_score)*100
    # print(array)
print(sum(array)/len(array))