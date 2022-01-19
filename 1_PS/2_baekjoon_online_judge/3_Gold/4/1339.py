"""
Date    : 2021.12.15
Update  : 2021.12.15
Source  : 단어 수학.py
Purpose : 문자열 문제인줄 알았으나, 수학 문제였음..
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
n = int(input())

arrays = []

for _ in range(n):
    temp = input()
    arrays.append(temp)

string_dict = dict()

for array in arrays:
    for i in range(len(array)):
        # 문자열을 key로 갖는 dict value에 현재 자리수만큼 더한다.
        if array[i] not in string_dict:
            string_dict[array[i]] = 10 ** (len(array) - i - 1)
        else:
            string_dict[array[i]] += 10 ** (len(array) - i - 1)

# 딕셔너리를 value 기준으로 내림차순 정렬하여 리스트로 만든다.
sort_dict = sorted(string_dict.items(), key=lambda x:x[1], reverse=True)

answer = 0

for i in range(9, -1, -1):
    k = 9 - i
    if len(sort_dict) > k:
        answer += i * sort_dict[k][1]

print(answer)