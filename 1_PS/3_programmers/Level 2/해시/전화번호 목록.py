"""
Date    : 2021.12.16
Update  : 2021.12.16
Source  : 전화번호 목록.py
Purpose : 문자열 비교를 통해 해결.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def solution(phone_book):
    answer = True

    phone_book.sort()

    for i, phone in enumerate(phone_book[:-1]):
        if phone in phone_book[i + 1]:
            answer = False
            break

    return answer

