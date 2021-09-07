n = int(input())
array = list(map(int, input().split()))
answer = []
sum_ar = sum(array)
for i in range(len(array)):
    for j in range(i+1, len(array)+1):
        answer.append(sum(array[i:j]))
print(answer)
result = 1e9
for i in range(1, sum_ar):
    if i not in answer:
        result = min(result, i)

print(result)

# 32분 53초 / Pass / 시간복잡도 초과할지도 모름. / 그리디에 대해 더 많이 풀어볼 것.