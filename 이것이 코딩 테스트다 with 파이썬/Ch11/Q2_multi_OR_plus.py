s = input()
answer = 1
for i in s:
    if int(i) == 0:
        pass
    else:
        answer *= int(i)

print(answer)

# 5분 / pass

s = input()
answer = 1
for i in s:
    if int(i) == 0:
        answer += int(i)
    else:
        answer *= int(i)

print(answer)

# 5분 / non-pass

