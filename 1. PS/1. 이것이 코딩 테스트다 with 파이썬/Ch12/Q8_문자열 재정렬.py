s = input()

str_array = []
int_array = 0

for i in range(len(s)):
    if s[i] >= 'A' and s[i] <= 'Z':
        str_array.append(s[i])
    elif s[i] >= '0' and s[i] <= '9':
        int_array += int(s[i])

str_array.sort()

print(*str_array, sep='', end='')
print(int_array)

str_array = []
int_array = 0

for i in range(len(s)):
    temp = ord(s[i])
    if temp >= 65 and temp <= 90:
        str_array.append(s[i])
    elif temp >= 48 and temp <= 57:
        int_array += int(s[i])

str_array.sort()

print(*str_array, sep='', end='')
print(int_array)

# 6분 13초 / pass