a, b, n = list(map(int, input().split()))

a = a % b
# answer = 0
if a == 0:
    print(0)
else:
    for i in range(n):
        a *= 10
        answer = a // b
        a = a%b

    print(answer)