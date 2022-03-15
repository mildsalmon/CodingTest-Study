"""
Date    : 2022.03.15
Update  : 2022.03.15
Source  : 20210.py
Purpose : 정렬 / timsort / re
url     : https://www.acmicpc.net/problem/20210
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
if __name__ == "__main__":
    n = int(input())
    strs = [input() for _ in range(n)]

    # strs.sort()
    # print(strs)

    for i in range(n):
        temp_str = []
        num = -1
        for s in strs[i]:
            if s.isalpha():
                if num != 0:
                    num = -1

                temp = ord(s) + 10000

                if temp >= ord('a') + 10000:
                    temp = temp - ord('a') + ord('A') + 0.5
                temp_str.append(temp)
            else:
                if num == -1:
                    num = len(temp_str)
                    temp_str.append(0)

                if s == '0':
                    temp_str[num] += 0.001
                else:
                    temp_str[num] += (ord(s) - ord('0') + 10)
        strs[i] = temp_str[:] + [strs[i]]

    # print(*strs, sep='\n')

    strs.sort(key=lambda x: x[:-1])

    print(*map(lambda x: x[-1], strs), sep='\n')
