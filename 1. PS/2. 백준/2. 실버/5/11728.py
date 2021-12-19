"""
Date    : 2021.12.19
Update  : 2021.12.19
Source  : 11728.py
Purpose : 투포인터 사용
url : https://www.acmicpc.net/problem/11728
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
n, m = list(map(int, input().split()))

# 두 배열은 정렬되어서 입력됨
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = []

A_pos = 0
B_pos = 0

#
while len(A) > A_pos and len(B) > B_pos:
    if A[A_pos] >= B[B_pos]:
        answer.append(B[B_pos])
        B_pos += 1
    elif A[A_pos] < B[B_pos]:
        answer.append(A[A_pos])
        A_pos += 1

if len(A) != A_pos:
    # answer.extend(A[A_pos:])
    print(*answer, sep=' ', end=' ')
    print(*A[A_pos:], sep=' ')
elif len(B) != B_pos:
    # answer.extend(B[B_pos:])
    print(*answer, sep=' ', end=' ')
    print(*B[B_pos:], sep=' ')
