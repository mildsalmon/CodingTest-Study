"""
Date    : 2022.02.27
Update  : 2022.02.27
Source  : 10. 2870.py
Purpose : 정규식
url     : https://www.acmicpc.net/problem/2870
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import re

if __name__ == "__main__":
    n = int(input())
    nums = []

    for i in range(n):
        word = input()

        word = re.sub(r'[\D]', ' ', word)
        nums.extend(map(int, word.split()))

    nums.sort()
    print(*nums, sep='\n')
