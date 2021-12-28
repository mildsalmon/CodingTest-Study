"""
Date    : 2021.12.28
Update  : 2021.12.28
Source  : 10546.py
Purpose : 해시를 이용하여 해결한다.
url     : https://www.acmicpc.net/problem/10546
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys

input = sys.stdin.readline

n = int(input())

participants = {}
p_hash = 0

for _ in range(n):
    temp = input()

    participants[hash(temp)] = temp
    p_hash += hash(temp)

for _ in range(n-1):
    temp = input()

    p_hash -= hash(temp)

print(participants[p_hash])
