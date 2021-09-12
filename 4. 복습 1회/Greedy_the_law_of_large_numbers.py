n, m, k = list(map(int, input().split()))
numbers = list(map(int, input().split()))

numbers.sort()

big_1 = numbers[-1]
big_2 = numbers[-2]

result = (m // (k+1)) * (big_1 * k + big_2) + big_1 * (m % (k+1))

print(result)