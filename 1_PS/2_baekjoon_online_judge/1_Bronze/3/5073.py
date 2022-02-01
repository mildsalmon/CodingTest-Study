"""
Date    : 2022.02.01
Update  : 2022.02.01
Source  : 5073.py
Purpose : 수학
url     : https://www.acmicpc.net/problem/5073
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":

    while True:
        num = list(map(int, input().split()))
        num.sort()

        if num[0] == 0 and num[1] == 0 and num[2] == 0:
            break

        if num[0] == num[1] and num[1] == num[2]:
            print("Equilateral")
        elif num[0] == num[1] or num[1] == num[2] or num[2] == num[0]:
            print("Isosceles")
        elif num[0] + num[1] <= num[2]:
            print("Invalid")
        else:
            print("Scalene")