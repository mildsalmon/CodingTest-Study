s = input()

first = s[0]
pre = s[0]
count = 0
for i in range(len(s)):
    if s[i] != pre and s[i] != first:
        count += 1
    pre = s[i]

print(count)

# 11분 / pass

s = input()

first = "1"
second = "0"
pre = s[0]
count_f = 0
count_s = 0

if s[0] == "0":
    count_f += 1
else:
    count_s += 1

for i in range(len(s)):
    if s[i] != pre and s[i] != first:
        count_f += 1
    if s[i] != pre and s[i] != second:
        count_s += 1
    pre = s[i]

print(min(count_s,count_f))

# 11분 / pass