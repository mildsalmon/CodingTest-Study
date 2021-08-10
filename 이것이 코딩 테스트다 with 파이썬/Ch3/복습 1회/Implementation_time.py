# 소요시간 : 20분

n = input()

hh = str(0)
mm = str(00)
ss = str(00)

time = hh + mm + ss
count = 0

while time != n + '5959':
    for i in time:
        if i == '3':
            count = count + 1
            break

    ss = int(ss)
    mm = int(mm)
    hh = int(hh)

    ss = ss + 1
    if ss == 60:
        ss = ss - 60
        mm = mm + 1
    if mm == 60:
        mm = mm - 60
        hh = hh + 1

    time = str(hh) + str(mm) + str(ss)

print(count)

n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)
            if '3' in time:
                count = count + 1

print(count)