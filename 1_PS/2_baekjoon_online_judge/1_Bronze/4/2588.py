a = int(input())
b = (input())
answer = [0] * 4
for i in range(len(b)):
    answer[i] = (a*int(b[2-i]))
    answer[-1] = answer[-1] + answer[i]*(10**i)
print(*answer, sep='\n')
