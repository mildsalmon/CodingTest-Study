"""
Date    : 2022.03.02
Update  : 2022.03.02
Source  : 21925.py
Purpose : dp / slice
url     : https://www.acmicpc.net/problem/21925
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

'''
Test Case

############################
Input
10
1 1 5 5 0 7 0 5 5 5

Output
-1

Answer
-1
############################
Input
8
1 2 3 3 3 3 2 1

Output
-1

Answer
1
############################
Input
6
1 2 2 1 1 1

Output
1

Answer
2
'''

if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))

    dp = []
    count = 0

    for num in array:
        dp.append(num)

        if len(dp) % 2 == 0:
            if dp == dp[::-1]:
                dp = []
                count += 1
            else:
                count = -1

    if count == 0:
        print(-1)
    else:
        print(count)

