x = int(input())
counts = []

num = [2, 3, 5]

for i in num:
    count = 0
    x_2 = x
    while x_2 > 1:
        if x_2 >= i:
            x_2 = (x_2 // i) + (x_2 % i)
        else:
            x_2 = x_2 - 1
        count = count + 1
    counts.append(count)
    # print(counts)
print(min(counts))

# 17분 54초