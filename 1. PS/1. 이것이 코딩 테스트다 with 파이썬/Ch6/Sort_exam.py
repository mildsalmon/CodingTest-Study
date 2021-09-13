# n = int(input())
student = []

n = 2
v = [['홍길동', 95],
     ['이순신', 77]]

for i in range(n):
    # student.append(list(map(str, input().split())))
    student.append(list(map(str, v[i])))

result = sorted(student, key=lambda x:x[1])

for i in range(n):
    print(result[i][0], end=' ')