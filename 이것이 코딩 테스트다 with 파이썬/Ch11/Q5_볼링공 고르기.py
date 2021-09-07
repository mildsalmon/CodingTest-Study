from itertools import combinations

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))
count_sort = [0] * (m+1)
result = 0

for i in array:
    count_sort[i] += 1

for i in range(1, len(count_sort)):
    if count_sort[i] > 0:
        count_sort[i] -= 1
print(count_sort)
for i in count_sort:
    if i < 2:
        result += i
    else:
        result *= i
print(result)
result = len(list(combinations(array, 2))) - result

print(result)

# 17분 14초 / non-pass

# 반례
# 5 3
# 1 1 1 2 3
# 10 8
# 1 1 2 3 3 8 4 8 8 2

################################################################
#################반례 적용하여 수정한 버전###########################
################################################################

combi = list(combinations(array, 2))
# print(combi)

answer = len(combi)

for i in combi:
   A, B = i
   if A == B:
       answer -= 1

print(answer)