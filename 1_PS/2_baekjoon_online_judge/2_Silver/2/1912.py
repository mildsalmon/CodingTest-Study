"""
Date    : 2021.12.30
Update  : 2021.12.30
Source  : 1912.py
Purpose : n이 10만일때의 dp
url     : https://www.acmicpc.net/problem/1912
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = array[:]

for i in range(1, n):
    dp[i] = max(array[i], dp[i-1] + array[i])

print(max(dp))