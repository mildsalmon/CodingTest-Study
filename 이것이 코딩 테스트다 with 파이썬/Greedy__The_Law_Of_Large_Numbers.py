
n, m, k = map(int, input().split(" "))

number = []
number = map(int, input().split(" "))

big_1 = 0
big_2 = 0

for i in number:
    if i > big_2:
        if i > big_1:
            big_2 = big_1
            big_1 = i
        else:
            big_2 = i
    print(big_1, big_2)

sum = 0

for j in range(1, m+1):
    big_cho = 0

    if j % (k+1) == 0:
        big_cho = big_2
    else:
        big_cho = big_1
    sum = sum + big_cho

    print(big_cho)
