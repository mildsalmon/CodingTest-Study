"""
Date    : 2021.12.19
Update  : 2021.12.19
Source  : 11728.py
Purpose : 리스트의 extend 함수 사용하여 해결. (속도 느림)
url : https://www.acmicpc.net/problem/11728
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
n, m = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.extend(B)
A.sort()

print(*A, sep=' ')