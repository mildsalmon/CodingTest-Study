n = int(input())

array = []

for i in range(n):
    array.append(int(input()))

avg = sum(array)/len(array)
avg = int(round(avg, 0))
mid = sorted(array)[len(array)//2]

count_sort = {}

for i in array:
    if i in count_sort:
        count_sort[i] += 1
    else:
        count_sort[i] = 1

max_count = sorted(count_sort.items(), key=lambda i:i[1], reverse=True)
# print(max_count)
# for key, value in count_sort.items():
mode_count = [x[0] for x in max_count if x[1] == max_count[0][1]]
if len(mode_count) > 1:
    mode_count = sorted(mode_count)[1]
else:
    mode_count = mode_count[0]
# bin =
scope = max(array) - min(array)

print(avg)
print(mid)
print(mode_count)
print(scope)