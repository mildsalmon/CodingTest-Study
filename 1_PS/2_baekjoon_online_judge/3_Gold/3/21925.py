"""
Date    : 2022.03.02
Update  : 2022.03.05
Source  : 21925.py
Purpose : dp / slice
url     : https://www.acmicpc.net/problem/21925
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    temp = []
    cnt = 0

    for i in array:
        temp.append(i)

        if len(temp) % 2 == 0:
            if temp == temp[::-1]:
                cnt += 1
                temp = []

    if temp:
        print(-1)
    else:
        print(cnt)