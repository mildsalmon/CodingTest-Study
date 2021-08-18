# n, k = list(map(int, input().split()))

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

n, k = 5, 3

A = [1, 2, 5, 4, 3]
B = [5, 5, 6, 6, 5]

A.sort()
B.sort(reverse=True)

print(A)
print(B)

for i in range(k):
    A[i], B[i] = B[i], A[i]

result = sum(A)

print(result)