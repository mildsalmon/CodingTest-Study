"""
Date    : 2022.02.13
Update  : 2022.02.13
Source  : 2075.py
Purpose : 자료구조 / 정렬 / 우선순위 큐
url     : https://www.acmicpc.net/problem/2075
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":
    n = int(input())
    array = []

    for _ in range(n):
        temp = list(map(int, input().split()))
        array.extend(temp)
        array.sort(reverse=True)
        array = array[:n]

    print(array[n-1])