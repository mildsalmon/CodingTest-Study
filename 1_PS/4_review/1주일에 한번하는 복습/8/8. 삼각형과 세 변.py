"""
Date    : 2022.02.06
Update  : 2022.02.06
Source  : 5073.py
Purpose : 수학
url     : https://www.acmicpc.net/problem/5073
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":
    while True:
        temp = list(map(int, input().split()))

        if temp[0] == 0 and temp[1] == 0 and temp[2] == 0:
            break

        temp.sort()

        if temp[0] + temp[1] <= temp[2]:
            print("Invalid")
        else:
            if temp.count(temp[0]) == 3:
                print("Equilateral")
            elif temp.count(temp[0]) == 2 or temp.count(temp[1]) == 2 or temp.count(temp[2]) == 2:
                print("Isosceles")
            else:
                print("Scalene")