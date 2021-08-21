import sys

n = int(input())
my_part = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
customer_part = list(map(int, sys.stdin.readline().rstrip().split()))
result = []

for i in customer_part:
    if i not in my_part:
        result.append("no")
    else:
        result.append("yes")

print(result)