n = int(input())

dp = []
i = 0
for i in range(1023):
# while True:
    temp = str(i)

    pre = temp[0]
    flag = True

    for j in temp[1:]:
        if int(pre) > int(j):
            pre = j
            flag = True
        else:
            flag = False
            break

    if flag:
        dp.append(i)
        i += 1
    else:
        i //= 10
        i *= 10
        i += 10

    if len(dp) == n + 1:
        break
    # print(dp)

if n < 1023:
    print(dp[-1])
else:
    print(-1)