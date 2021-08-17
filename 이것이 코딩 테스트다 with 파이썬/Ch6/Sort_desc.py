n = int(input())
number = []

for i in range(n):
    number.append(input())

number.sort(reverse=True)

print(' '.join(number))