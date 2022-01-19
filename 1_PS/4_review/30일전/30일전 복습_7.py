# 성적이 낮은 순서로 학생 출력하기

n = int(input())
array = {}

for i in range(n):
    temp = list(input().split())

    array[temp[0]] = int(temp[1])

answer = sorted(array.items(), key=lambda x:x[1])

print(*list((lambda *x: x[0])(zip(*answer)))[0], sep=' ')