"""
Date    : 2022.03.02
Update  : 2022.03.02
Source  : 21925.py
Purpose : dp / slice
url     : https://www.acmicpc.net/problem/21925
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))

    dp = []
    count = 0
    flag = False

    for num in array:
        dp.append(num)

        if len(dp) % 2 == 0:
            if dp == dp[::-1]:
                dp = []
                count += 1
                flag = False
            else:
                flag = True

    if flag:
        print(-1)
    else:
        print(count)
