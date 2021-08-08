import time

start = time.time()

n, k = list(map(int, input().split()))

count = 0

while n != 1:
  if n % k == 0:
    n = n // k
  elif n % k != 0:
    n = n - 1
  count = count + 1

end = time.time()

total = end - start

print(count)



# n, k = map(int, input().split())
# result = 0

# while n >= k:
#   while n % k != 0:
#     n -= 1
#     result += 1
#   n //= k
#   result += 1

# while n > 1:
#   n -= 1
#   result += 1

# end = time.time()

# total = end - start

# print(result)

print(total)