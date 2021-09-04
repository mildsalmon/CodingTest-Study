x = int(input())
total_count = 0

for i in range(1, x+1):
    str_a = str(i)#list(map(int, str(i)))
    # d = 0
    if len(str_a) > 1:
        d = int(str_a[1:2]) - int(str_a[0:1])
        count = 0
        for j in range(1, len(str_a)):
            if int(str_a[j]) - int(str_a[j-1]) == d:
                count += 1
    else:
        count = 0
    if count == len(str_a)-1:
        total_count += 1

print(total_count)

# 문제 이해가 어려웠던 문제.

# - 1~N까지 for문에 돌리면서 각 자리수를 1의 자리 숫자로 보고 등차를 구해서 등차가 반복된다면 성공. 아니면 실패.