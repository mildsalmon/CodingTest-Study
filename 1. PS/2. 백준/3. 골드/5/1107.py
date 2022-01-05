"""
Date    : 2022.01.05
Update  : 2022.01.05
Source  : 리모컨.py
Purpose :
url     : https://www.acmicpc.net/problem/1107
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":
    n: int = int(input())
    m: int = int(input())

    if m:
        trouble_button = set(map(int, input().split()))
    else:
        trouble_button = set()

    max_channel = 500_000
    min_push_button = abs(100 - n)

    if min_push_button:
        for i in range(max_channel * 2 + 1):
            flag = True
            count = 0

            for j in map(int, str(i)):
                if j in trouble_button:
                    flag = False
                    break
                else:
                    count += 1
            if flag:
                min_push_button = min(min_push_button, count + abs(n - i))

    print(min_push_button)