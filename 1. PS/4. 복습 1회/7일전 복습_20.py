# Ch11_그르디_볼링공 고르기

from itertools import combinations

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

combination_array = list(combinations(array, 2))
len_combination = len(combination_array)

for combination in combination_array:
    a, b = combination
    if a == b:
        len_combination -= 1

print(len_combination)