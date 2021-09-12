A = input()
oper_stack = []
answer = ""

def priority(oper):
    if oper == "*" or oper == "/":
        return 2
    elif oper == "+" or oper == "-":
        return 1
    else:
        return 0

for i in A:
    if i.isalpha():
        answer += i
        continue

    if i == "(":
        oper_stack.append(i)
    elif i == ")":
        while(True):
            if oper_stack and oper_stack[-1] != "(":
                answer += oper_stack.pop()
            else:
                oper_stack.pop()
                break
    else:
        while(True):
            if oper_stack and priority(oper_stack[-1]) >= priority(i):
                answer += oper_stack.pop()
            else:
                oper_stack.append(i)
                break
    # print(answer)
    # print(oper_stack)

while oper_stack:
    answer += oper_stack.pop()

print(answer)