k = int(input())
s = list(input())

answer = ''

for i in range(len(s)):
    if i % k == 0:
        answer += s[i]

print(answer)