n = int(input())

array = []
avg = []
avg_per = [0] * (n)

for i in range(n):
    A = list(map(int, input().split()))
    array.append(A[1:])
    avg.append(sum(array[i])/len(array[i]))

    for j in array[i]:
       if j > avg[i]:
           avg_per[i] += 1
    # print(avg_per)
    avg_per[i] = (avg_per[i] / len(array[i])) * 100

for i in avg_per:
    print("{0:.3f}%".format(i))