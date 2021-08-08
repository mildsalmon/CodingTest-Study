# n = 1260
# count = 0

# for i in [500, 100, 50, 10]:
#   count = count + (n // i)
#   n = n - (n // i) * i

# print(count)

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n // coin
  n %= coin

print(count)