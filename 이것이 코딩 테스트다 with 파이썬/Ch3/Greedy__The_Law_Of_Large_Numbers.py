n, m, k = list(map(int, input().split()))

arr = list(map(int, input().split()))

# n, m, k = 5, 8, 3

# arr = [2,4,5,4,6]

arr = sorted(arr, reverse=True)
print(arr)
k_k = 0
result = 0
point = 0

for i in range(m):
  
  if k_k < k:
    k_k = k_k + 1
    point = 0
  elif k_k == k:
    k_k = 0
    point = 1

  result = arr[point] + result
  # print(result)

print(result)