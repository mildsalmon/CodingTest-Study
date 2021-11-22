A = input()
B = input()
answer = 0

point = 0

if len(A) < len(B):
    # 삽입
    answer += len(B) - len(A)
# elif len(A) > len(B):
#     # 삭제
#     answer += len(A) - len(B)

for i in range(len(A)):
    # `ssy`에서 `s`같이 중복되는 문자열을 방지하기 위해서, [point:]을 함
    if A[i] in B[point:]:
        point = B.index(A[i]) + 1
    else:
        # 교체
        answer += 1

print(answer)